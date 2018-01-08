import gear

def check_request_status(job):
    if job.complete:
        print "Job %s finished!  Result: %s" % (job.name, job.data)
    elif job.warning:
        print "Job %s warning! exception: %s" % (job.name, job.exception)
    elif job.failure:
        print "Job %s failed! exception: %s" % (job.name, job.exception)

client = gear.Client()
client.addServer('192.168.122.89')
client.waitForServer()
job = gear.Job("reverse", "test string")
client.submitJob(job)

check_request_status(job)
