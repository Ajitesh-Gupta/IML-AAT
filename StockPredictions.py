m, k, d = map(float, input().split())
prev = {}
moneysold = int()
for x in range(int(d)):
    for i in range(int(k)):
        owen = []
        n = int(0)
        name, owend, a, b, c, d, e = input().split()
        owend = int(0)
        e = float(e)
        if float(e) == max(float(a), float(b), float(c), float(d), float(e)):
            if int(owend) > int(0):
                n += 1
                moneysold = int(int(e) * int(owend))
                owend = int(0)
                prev[name] = (int((m) / int(e)), 'SELL')
                owen.append(name)
        elif float(e) == min(float(a), float(b), float(c), float(d), float(e)):
            if int(moneysold) > int(0):
                n += 1
                o = int((moneysold) / int(e))
                while o > moneysold:
                    o -= 1
                prev[name] = (o, 'BUY')
                moneysold = int(int(moneysold) - int(moneysold) / float(e))
                owend += int((moneysold) / int(e))
                owen.append(name)
            else:
                if int(int(m) / float(e)) > 0:
                    n += 1
                    o = int((m) / int(e))
                    while o*float(e) > m:
                        o -= 1
                    prev[name] = (o, 'BUY')
                    m = int(int(m) - int(m) / float(e))
                    owend += int((m) / int(e))
                    owen.append(name)
        elif name in prev.keys():
            if prev[name][0] < float(e):
                n += 1
                prev[name][1] = 'SELL'
                moneysold = int(e) * int(ownend)
                owend = int(0)
    print(n)
    for y in range(n):
        print("%s %s %d" % (owen[y], prev[owen[y]][1], prev[owen[y]][0]))