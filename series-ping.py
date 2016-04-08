import commands
for i in range(100):
    value = commands.getoutput('python get_ping_rate.py')
    print "Step", i, "...", value
    commands.getoutput('echo %s\t%s >> series.log' % (i, value))
