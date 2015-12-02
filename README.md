Collects JSON objects from a beanstalkd queue and stores the data into the elasticsearch

Install beanstalkd 
1)sudo apt-get install beanstalkd 
2) pip install pyyaml 
3) pip install beanstalkc

Run Beanstalkd
beanstalkd -l 127.0.0.1 -p 11301 &

Documentation
http://beanstalkc.readthedocs.org/en/latest/tutorial.html#tube-management

