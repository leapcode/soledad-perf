import commands
import datetime

# How many points to measure. Make sure that you leave the baseline
# running for a significative amount before triggering the sync, it's possible 
# you have significant variability in there.
POINTS = 200

commands.getoutput('echo time req/s cpu mem phase > series.log')
start = datetime.datetime.now()

for i in range(POINTS):
    value = commands.getoutput('python get_ping_rate.py')
    print "Step", i, "...", value
    stats = commands.getoutput('python get_client_cpu_mem.py')
    cpu, mem, phase = stats.split()
    now = datetime.datetime.now()
    secs = (now - start).total_seconds()
    commands.getoutput(
        'echo %s\t%s\t%s\t%s\t%s >> series.log' % (secs, value, cpu, mem, phase))
