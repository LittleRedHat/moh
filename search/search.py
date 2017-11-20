from elasticsearch import Elasticsearch


class Searcher(object):
    def __init__(self, hosts):
        self.es = Elasticsearch(hosts=hosts)

        
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
                        "field": "content",
                        "indexed_chars": -1
                    }
                }
            ]
        }
        return self.es.ingest.put_pipeline(id='attachment',body=pipeline_params)

    def es_search(self,index,doc_type,query):
        results = self.es.search(index=index,doc_type=doc_type,body=query)
        return results


