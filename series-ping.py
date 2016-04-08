import commands
import datetime

POINTS = 100

start = datetime.datetime.now()

for i in range(POINTS):
    value = commands.getoutput('python get_ping_rate.py')
    print "Step", i, "...", value
    cpu_mem = commands.getoutput('python get-client-cpu-mem.py')
    cpu, mem = cpu_mem.split()
    now = datetime.datetime.now()
    secs = (now - start).seconds
    commands.getoutput(
        'echo %s\t%s\t%s\t%s >> series.log' % (secs, value, cpu, mem))
