#-*- coding=utf-8 -*-
from flask import Flask,request,jsonify
from flask_cors import CORS
from search.search import Searcher
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:danshi@localhost:3306/moh'
db = SQLAlchemy(app)

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
    keywords = db.Column(db.String(8192),nullable=True)




###############################################
# elasticsearch 初始化
###############################################
@app.route('/moh/es/init',)
def es_init():
    pass

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
    print qfilters
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
                        "inline":"if(doc['type'].value == 'html'){return doc['publish.keyword'].value} return doc['attachment.date'].value",
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
                        "inline":"if(doc['type'].value == 'html'){return doc['publish.keyword'].value} return doc['attachment.date'].value",
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
                "field":"nation.keyword"
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
                "include":["location","nation","publish","type","url","local_url","attachment","title","language","url"],
                "exclude":["attachment.content","content"]
        },
        "sort":sort_dsl,
        'from':qfrom,
        'size':qsize
    }
    es = Searcher(["127.0.0.1:9200"])
    cursor = es.es_search("crawler","articles",dsl)
    results = cursor['hits']['hits'][qfrom:(qfrom+qsize)]
    total = cursor['hits']['total']
    nation_buckets = cursor['aggregations']['group_by_nation']['buckets']

    jresult = []
    for item in results:
        obj = item['_source']
        obj['score'] = item['_score']
        jresult.append(obj)

    return jsonify({'records':jresult,'total':total,'nation_distribution':nation_buckets})

###############################################
# 用户登录
###############################################
@app.route('/moh/user/login',methods=['POST'])
def login():
    username = request.values.get('username')
    password = request.values.get('password')
    user = User.query.filter_by(username=username).filter_by(password=password)


###############################################
# 文档/附件搜索历史摘要统计
###############################################
@app.route('/moh/history',methods=['GET'])
def history():
    pass


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=9000)

