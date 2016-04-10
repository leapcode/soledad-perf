import commands
import urllib
import psutil

pid = urllib.urlopen('http://localhost:8080/pid').read()
res = commands.getoutput("ps -p " + pid + " -o \%cpu,\%mem")
splitted = res.split()
cpu = splitted[2]
mem = splitted[3]

print cpu, mem
