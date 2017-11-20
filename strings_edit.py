def semifold(ss, f, g):
    # сворачиваем список, но не до конца, а только в случаях, когда верно условие f(ss[i], ss[i+1])
    # предполагается, что если f(ss[i], ss[i+1]) и f(ss[i+1], ss[i+2]), то f (g(ss[i], ss[i+1]), ss[i+2])
    # эдакая транзитивность!

    # не спрашивайте, зачем я это делаю.
    if len(ss) < 2:
        return ss
    if f(ss[0], ss[1]):
        return semifold([g(ss[0], ss[1])]+ss[2:], f, g)
    else:
        return [ss[0]] + semifold(ss[1:], f, g)

def myf(x, y):
    return x[1]==y[1]

def myg(x, y):
    return (x[0]+y[0], x[1])

def simple_add(s1, s2):
    #определяем вставки, которые нужно сделать, чтобы получить в начале строки s1 строку s2
    #на удаления забиваем болт, только вставки :)
    #на то, что у s1 может остаться хвост, забиваем болт
    #памяти, вообще говоря, мало (нельзя запихнуть любую из строк целиком)
    if len(s2) == 0:
        return []
    if len(s1) == 0:
        return [(s2,0)]
    i=0
    j=0
    add = ''
    add_list=[]
    add_length = 0
    while (j < len(s2) and j-add_length < len(s1)):
        if s1[j-add_length] != s2[j]:
            add_list.append((s2[j], j-add_length))
            add_length = add_length + 1
        j = j+1
    add_list = semifold(add_list, myf, myg)
    return add_list