def a_1():
    file = open('atencion.txt', 'r')
    data = file.readlines()
    file.close()
    for x in data:
        print(x.strip())


def a_2():
    countgen = 0
    pond = [.15, .1, .2, .2, .25, .03, .07]
    proc, proc2 = [], []
    file = open('atencion.txt', 'r')
    data = file.readlines()
    file.close()
    for x in data:
        count = 2
        spl = x.strip().split(';')
        pre = []
        while count < 9:
            pre.append(spl[count])
            count += 1
        proc.append(pre)
    for x in proc:
        count = 0
        pre = []
        while count < 7:
            res = eval(x[count])*pond[count]
            pre.append("%.2f" % res)
            count += 1
        proc2.append(pre)


def a_3():
    pond = [.15, .1, .2, .2, .25, .03, .07]
    proc, proc2, new = [], [], []
    file = open('atencion.txt', 'r')
    data = file.readlines()
    file.close()
    for x in data:
        count = 2
        spl = x.strip().split(';')
        pre = []
        while count < 9:
            pre.append(spl[count])
            count += 1
        proc.append(pre)
    for x in proc:
        count = 0
        pre = []
        while count < 7:
            res = eval(x[count])*pond[count]
            pre.append("%.2f" % res)
            count += 1
        proc2.append(pre)
    for x in proc2:
        new.append(max(x, key=float))
    print(max(new, key=float))


def a_4():
    pond = [.15, .1, .2, .2, .25, .03, .07]
    proc, proc2, new = [], [], []
    file = open('atencion.txt', 'r')
    data = file.readlines()
    file.close()
    for x in data:
        count = 2
        spl = x.strip().split(';')
        pre = []
        while count < 9:
            pre.append(spl[count])
            count += 1
        proc.append(pre)
    for x in proc:
        count = 0
        pre = []
        while count < 7:
            res = eval(x[count])*pond[count]
            pre.append("%.2f" % res)
            count += 1
        proc2.append(pre)
    for x in proc2:
        for y in x:
            new.append(y)
    print(sorted(new, reverse=True, key=float))


def a_5(val):
    pond = [.15, .1, .2, .2, .25, .03, .07]
    proc, proc2, new = [], [], []
    file = open('atencion.txt', 'r')
    data = file.readlines()
    file.close()
    for x in data:
        count = 2
        spl = x.strip().split(';')
        pre = []
        while count < 9:
            pre.append(spl[count])
            count += 1
        proc.append(pre)
    for x in proc:
        count = 0
        pre = []
        while count < 7:
            res = eval(x[count])*pond[count]
            pre.append("%.2f" % res)
            count += 1
        proc2.append(pre)


a_2()
