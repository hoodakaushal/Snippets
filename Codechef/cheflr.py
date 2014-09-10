__author__ = 'hooda'


def node_num(path):
    num = 1
    x = 1000000007
    for fork in path:
        if num % 2 == 0:
            # print("even")
            if fork == "l":
                num = (2 * num - 1)
                # print("2x-1")
            else:
                num = (2 * num + 1)
                # print("2x+1")
        else:
            # print("odd")
            if fork == "l":
                num = (2 * num)
                # print("2x")
            else:
                num = (2 * num + 2)
                # print("2x+2")
    return num % x


def runner():
    cases = int(raw_input())
    paths = []
    for i in range(0, cases):
        paths += [raw_input()]
    for path in paths:
        print(node_num(path))
    return

# runner()

import subprocess


def crun(s):
    program = "cheflr.exe"
    piddi = subprocess.Popen([program, s], stdout=subprocess.PIPE)
    out, err = piddi.communicate()
    return out.replace("\n", "").replace("\r", "")


def comparator():
    query = ""
    flag = True
    while flag:
        query += "r"
        flag = match(query)
    print(query)


def qgen(n):


def match(query):
    piddi = crun(query)
    me = str(node_num(query))
    print(me, piddi)
    return piddi == me


comparator()
#print(node_num('rrlrlrlrrlrlrlrlrrlrlllrlrrrrrrllrrlrlrlrlrlrlrrlrlrlrlrlrlrlrlrllrlrllrllrlrllrllrllrlrlrlrllrlrlrlrllrlrlrlllllllllllrllrrlrllrlrlrlrlrlrllrlrlrlrllrlrlrlrllrlrlrlrlrllrlrlrlrllrlrlrlrllrlrllrlrrrrrrrllllllllllllllllllllllllllllrrrrrrrrrrrrrrlllrllllllllllllllrrrrrrrrrrrlllllllllllllllllrrrrrrrrrrrrrrrrrrrrrrrrrlllllllllllllllllllrrrrrrrrrrllllllrlrlrrlrlrlrlrrlrlllrlrrrrrrllrrlrlrlrlrlrlrrlrlrlrlrlrlrlrlrllrlrllrllrlrllrllrllrlrlrlrllrlrlrlrllrlrlrlllllllllllrllrrlrllrlrlrlrlrlrllrlrlrlrllrlrlrlrllrlrlrlrlrllrlrlrlrllrlrlrlrllrlrllrlrrrrrrrllllllllllllllllllllllllllllrrrrrrrrrrrrrrlllrllllllllllllllrrrrrrrrrrrlllllllllllllllllrrrrrrrrrrrrrrrrrrrrrrrrrlllllllllllllllllllrrrrrrrrrrllllllrlrlrrlrlrlrlrrlrlllrlrrrrrrllrrlrlrlrlrlrlrrlrlrlrlrlrlrlrlrllrlrllrllrlrllrllrllrlrlrlrllrlrlrlrllrlrlrlllllllllllrllrrlrllrlrlrlrlrlrllrlrlrlrllrlrlrlrllrlrlrlrlrllrlrlrlrllrlrlrlrllrlrllrlrrrrrrrllllllllllllllllllllllllllllrrrrrrrrrrrrrrlllrllllllllllllllrrrrrrrrrrrlllllllllllllllllrrrrrrrrrrrrrrrrrrrrrrrrrlllllllllllllllllllrrrrrrrrrrllllllrlrlrrlrlrlrlrrlrlllrlrrrrrrllrrlrlrlrlrlrlrrlrlrlrlrlrlrlrlrllrlrllrllrlrllrllrllrlrlrlrllrlrlrlrllrlrlrlllllllllllrllrrlrllrlrlrlrlrlrllrlrlrlrllrlrlrlrllrlrlrlrlrllrlrlrlrllrlrlrlrllrlrllrlrrrrrrrllllllllllllllllllllllllllllrrrrrrrrrrrrrrlllrllllllllllllllrrrrrrrrrrrlllllllllllllllllrrrrrrrrrrrrrrrrrrrrrrrrrlllllllllllllllllllrrrrrrrrrrlllll'))