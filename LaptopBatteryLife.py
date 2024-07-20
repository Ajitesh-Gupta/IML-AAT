import sys
d=sys.stdin.readlines()
if float(d[0])*2.0 > 8.0:
    print(8.0)
else:
    print(float(d[0])*2.0)
