__author__ = 'hooda'

def deleter(s):
    dels = 0
    while len(s) > 0:
        print(s)
        i = 0
        while i+1 < len(s) and s[i] == s[i+1]:
            i += 1
        if i > 0:
            dels += i
        s = s[i+1:]
    return dels

def runner():
    t = int(raw_input())
    for i in range(0, t):
        s = raw_input()
        print(s)
        print(deleter(s))
    return

runner()
