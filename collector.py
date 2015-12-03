import beanstalkc
import json
from varlib import MYHOST
from elasticsearch import Elasticsearch

def main():
    beanstalk = beanstalkc.Connection(host=MYHOST, port=11301)
    es = Elasticsearch()

    # ignore 400 cause by IndexAlreadyExistsException when creating an index
    es.indices.create(index='grmoto', ignore=400)

    # ignore 404 and 400
    es.indices.delete(index='grmoto', ignore=[400, 404])


    try:
        while True:
            # To receive a job:
            job = beanstalk.reserve()
        
#           if job.body == 'quit':
#               print 'The agent shutting down'
#               break


            # Work with the job:
            obj = json.loads(job.body)
            
            #print json.dumps(obj, sort_keys=True, indent=4, separators=(',',': '))

            #use elastic search 
            res = es.index(index='grmoto', doc_type='native_objects', body = obj)
            print(res['created'])
            
            #Release the job
            job.delete()
    except:
        again()


def again():
    main()


if __name__ == "__main__":
    main()

