from elasticsearch import Elasticsearch


class Searcher(object):
    def __init__(self, hosts):
        self.es = Elasticsearch(hosts=hosts)
    
    def es_mapping(self,index,doc_type,mapping):
        return self.es.indices.put_mapping(index=index,doc_type=doc_type,body=mapping)
    

    def es_setting(self,index,setting):
        return self.es.indices.put_setting(index=index,body=setting)
        
        


        
    def delete_by_query(self,index,doc_type,query):
        return self.es.delete_by_query(index=index,doc_type=doc_type,body=query)

    def es_init(self):
        # create index mapping
        # self.es.indices.create()
        # create ingest pipeline

        pipeline_params = {
            "description": "attachent extractor pipeline",
            "processors": [
                {
                    "attachment": {
                        "field": "data",
                        "indexed_chars": -1
                    }
                }
            ]
        }
        return self.es.ingest.put_pipeline(id='attachment',body=pipeline_params)

    def es_search(self,index,doc_type,query):
        results = self.es.search(index=index,doc_type=doc_type,body=query)
        return results


