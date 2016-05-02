import commands
import urllib
import psutil

pid, phase = urllib.urlopen('http://localhost:8080/stats').read().split()
res = commands.getoutput("ps -p " + pid + " -o \%cpu,\%mem")
splitted = res.split()
cpu = splitted[2]
mem = splitted[3]

print cpu, mem, phase
