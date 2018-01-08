import gear

def task_listener_reverse(gearman_worker, gearman_job):
    print 'Reversing string: ' + gearman_job.data
    return gearman_job.data[::-1]

worker = gear.Worker('reverser')
worker.addServer('192.168.122.89')
worker.registerFunction('reverse')

while True:
    job = worker.getJob()
    job.sendWorkComplete(job.arguments[::-1])
