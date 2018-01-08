# job-pusher
A project for reading from one host, doing some processing, and writing to another from a pool of hosts.

# Usage

Start the server:
gearmand --log-file log/gearmand/gearmand.log --listen <ip> --verbose=INFO

python worker.py

python client.py # puts one job on the queue

# Output

$ python client.py 
Job reverse finished!  Result: ['gnirts tset']
