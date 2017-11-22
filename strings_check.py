# http(s)://hostname(:port)/path/to/page?param1=value1&param2=value2&param1=value3

def myfunc(l):
    return l.split("=")

def gethost(l):
    return l.split("?")[0]

## считаем "diff" двух http-запросов
def httpdiff(s1, s2):
    h1 = gethost(s1)
    h2 = gethost(s2)
    if h1 != h2:
        print("different hosts!!!")
        return None
    l1 = s1.split("?")[1]
    l1 = l1.split("&")
    l2 = s2.split("?")[1]
    l2 = l2.split("&")
    fff = lambda x: x.split("=")
    l1 = list(map(fff, l1))
    l2 = list(map(fff, l2)) 
    l1add = []
    l2add = []
    for x in l1:
        if x not in l2:
            l1add = l1add + [x]
    for x in l2:
        if x not in l1:
            l2add = l2add + [x]

    return (l1add, l2add)