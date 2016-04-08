import commands

pid = commands.getoutput('ps x | grep "[s]erver-solsync" | cut -d " " -f 2')
res = commands.getoutput("ps -p " + pid + " -o \%cpu,\%mem")
splitted = res.split()
cpu = splitted[2]
mem = splitted[3]

print cpu
print mem
