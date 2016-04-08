import commands
import re

res = commands.getoutput(
    'httperf --server localhost --port 8080 --num-calls 5 --num-conns 20 '
    '--uri /ping  | grep "Connection rate"')
print re.findall('[-+]?([0-9]*\.?[0-9]+)', res)[0]
