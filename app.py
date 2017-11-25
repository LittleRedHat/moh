#-*- coding=utf-8 -*-
from flask import Flask,request,jsonify
from flask_cors import CORS
from search.search import Searcher
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from datetime import datetime
import json
from datetime import timedelta

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:danshi@localhost:3306/moh'
db = SQLAlchemy(app)
migrate = Migrate(db)

manager = Manager(app)
manager.add_command('db',MigrateCommand)

###############################################
# 用户表
###############################################
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),unique=True,nullable=False)
    password = db.Column(db.String(1024),nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username
###############################################
# 搜索记录表
###############################################
class Record(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    keyword = db.Column(db.String(4096))
    result = db.Column(db.String(4096))
    when = db.Column(db.DateTime)

    def __init__(self,keyword,result,when=None):
        self.keyword = keyword
        self.result = result
        self.when = when or datetime.now()
    def __repr__(self):
        return '<Record %r>' %(self.result)

# class Result(db.Model):
#     id = db.Column(db.Integer,primary_key = True)
#     result = db.Column(db.)

###############################################
# mysql 初始化
###############################################
@app.route('/moh/db/init')
def db_init():
    db.create_all()
    return jsonify({'code':200})
@app.route('/moh/db/drop')
def db_drop():
    db.drop_all()
    return jsonify({'code':200})

###############################################
# elasticsearch 初始化
###############################################
@app.route('/moh/es/init')
def es_init():
    es = Searcher(["127.0.0.1:9200"])
    mapping = {
        "properties":{
            "nation":{
                "type":"keyword"
            },
            "type":{
                "type":"keyword"
            },
            "local_url":{
                "type":"keyword"
            },
            "url":{
                "type":"keyword"
            },
            "publish":{
                "type":"date",
                "format":"YYYY-MM-DD'T'HH:mm:ssZ"
            },
            "language":{
                "type":"keyword"
            },
            "location":{
                "type":"keyword"
            }
        }
    }
    return jsonify(es.es_mapping('crawler','articles',mapping))

###############################################
# 文档/附件多语言搜索
###############################################
@app.route('/moh/es/search',methods=['POST'])
def search():
    content =  request.json
    qshoulds = content.get("should") or []
    qfrom = content.get("from") or 0
    qsize = content.get("size") or 20
    qfilters = content.get("filters") or []
    qsort = content.get("sort") or "all"
    ###############################################
    # 多语言查询支持
    ###############################################
    shoulds = []
    for item in qshoulds:
        musts = []
        for sentence in item:
            obj = {
                "multi_match":{
                    "query":sentence,
                    "minimum_should_match":"50%",
                    "fields":["content","attachment.content"]
                }
            }
            musts.append(obj)
        must_dsl = {
            "bool":{
                "must":musts
            }
        }
        shoulds.append(must_dsl)

    ###############################################
    # 过滤查询支持
    ###############################################
    # print qfilters
    filter_must = []
    for item in qfilters:
        name = item.get('name') or ''
        values = item.get('value') or []
        if 'all' in values or len(values) == 0:
            continue
        if not name in ['nation','language','type']:
            continue
        if name == 'language':
            filter_dsl = {
                "bool":{
                    "should":[
                        {
                            "terms":{
                                "language":values
                            }
                        },
                        {
                            "terms":{
                                "attachment.language":values
                            }
                        }
                    ]
                }
            }
        else:
            filter_dsl = {
                "terms":{
                    name:values
                }
            }
        filter_must.append(filter_dsl)

    filter_dsl = {
        "bool":{
            "must":filter_must
        }
    } 
    ###############################################
    # 排序支持
    ############################################### 
    sort_dsl = []
    if qsort == 'date':
        sort_dsl = [
            {
                "_script":{
                    "type":"string",
                    "script":{
                        "lang":"painless",
                        "inline":"if(doc['type'].value == 'html'){return doc['publish'].value} return doc['attachment.date'].value",
                    },
                    "order":"desc"
                }
            }
        ]
    elif qsort == 'score':
        sort_dsl = [
            {
               "_score":{
                   "order":"desc"
               } 
            }
        ]
    elif qsort == 'all':
        sort_dsl = [
            {
                "_script":{
                    "type":"string",
                    "script":{
                        "lang":"painless",
                        "inline":"if(doc['type'].value == 'html'){return doc['publish'].value} return doc['attachment.date'].value",
                    },
                    "order":"desc"
                }
            },
            {
               "_score":{
                   "order":"desc"
               } 
            }
        ]
    
    ###############################################
    # 聚合统计
    ###############################################
    aggs = {
        "group_by_nation":{
            "terms":{
                "field":"nation"
            },
        }

    }

    ###############################################
    # 查询语句
    ###############################################
    dsl = {
        "query":{
            "bool":{
                "should":shoulds,
                "minimum_should_match": 1,
                "filter":filter_dsl,
            },
        },
        "aggs":aggs,
        "_source":{
                "include":["location","nation","publish","type","url","local_url","attachment","title","language","keywords"],
                "exclude":["attachment.content","content"]
        },
        "sort":sort_dsl,
        'from':qfrom,
        'size':qsize
    }
    es = Searcher(["127.0.0.1:9200"])
    cursor = es.es_search("crawler","articles",dsl)
    results = cursor['hits']['hits']
    total = cursor['hits']['total']
    nation_buckets = cursor['aggregations']['group_by_nation']['buckets']

    jresult = []
    keywords = {}
    for item in results:
        obj = item['_source']
        obj['score'] = item['_score']
        ###############################################
        # 搜索历史记录
        ###############################################
        if obj['type'] == 'html':
            k = obj['keywords']
            try:
                k = json.loads(k)
                for item in k:
                    key = fuzzy_query(keywords,item[0])
                    if key:
                        keywords[key] += 1
                    else:
                        keywords[item[0]] = 1        
            except Exception,e:
                print e
        jresult.append(obj)
    record = Record(json.dumps(qshoulds),json.dumps(keywords))
    db.session.add(record)
    db.session.commit()
    return jsonify({'records':jresult,'total':total,'nation_distribution':nation_buckets})

###############################################
# 用户登录
###############################################
@app.route('/moh/user/login',methods=['POST'])
def login():
    username = request.values.get('username')
    password = request.values.get('password')
    user = User.query.filter_by(username=username).filter_by(password=password)
    if user:
        return jsonify({"code":200})
    else:
        return jsonify({"code":1001,"msg":"用户名或密码错误"})


###############################################
# 文档/附件搜索历史摘要统计
###############################################
@app.route('/moh/history',methods=['GET'])
def history():
    now = datetime.now()
    week = timedelta(days=-7)
    last_week = now + week
    last_week = last_week.strftime('%Y-%m-%d %H:%M:%S')
    records = Record.query.filter(Record.when >= last_week).all()
    result = {}
    for record in records:
        k = json.loads(record.result)
        
        for item in k:
            key = fuzzy_query(result,item)
            if key:
                result[key] += k.get(item) or 0
            else:
                result[item] = k.get(item) or 0
    return jsonify(result)


def fuzzy_query(obj,key):
    for item in obj.keys():
       if item.find(key) == 0 or key.find(item) == 0:
            return item
    return None    


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=9000)

