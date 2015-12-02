import beanstalkc
import json
from varlib import MYHOST


def main():
    beanstalk = beanstalkc.Connection(host=MYHOST, port=11301)


    while True:

        # To receive a job:
        job = beanstalk.reserve()
        
#       if job.body == 'quit':
#           print 'The agent shutting down'
#           break


        # Work with the job:
        obj = json.loads(job.body)
        
        print json.dumps(obj, sort_keys=True, indent=4, separators=(',',': '))


        job.delete()




if __name__ == "__main__":
    main()

