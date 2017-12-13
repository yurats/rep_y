# http(s)://hostname(:port)/path/to/page?param1=value1&param2=value2&param1=value3

def get_host_n_pars(l):
    if len(l.split("?")) == 0:
        return("", [])

    host = l.split("?")[0]

    if len(l.split("?")) > 1:
        pars_string = l.split("?")[1]
        # сделали список из строк вида "p1=v1"
        pars_list = pars_string.split("&")
        # сделали список вида [["p1", "v1"], ["p2", "v2"], ...]
        pars = list(map(lambda x: x.split("="), pars_list))
    else:
        pars = []
    return (host, pars)

## считаем "diff" двух http-запросов
def httpdiff(s1, s2):
    ss1 = get_host_n_pars(s1)
    ss2 = get_host_n_pars(s2)

    # проверили всякое
    # можно и сложнее проверки делать, в принципе...
    if (ss1[0] != ss2[0]):
        print("smth bad with hostnames")
        return None

    # собственно, разница.
    l1add = []
    l2add = []
    for x in ss1[1]:
        if x not in ss2[1]:
            l1add = l1add + [x]
    for x in ss2[1]:
        if x not in ss1[1]:
            l2add = l2add + [x]
    return (l1add, l2add)

def main():
    list1 = ["https://vk.com/im?sel=10866456", "https://vk.com/audios1491016", "https://vk.com/im?peers=c72_50348969&sel=68863"]
    list2 = ["https://vk.com/im?sel=50348969", "https://vk.com/audios50348969", "https://vk.com/im?peers=15763918_50348969&sel=c72"]
    for x in list(map(httpdiff, list1, list2)):
        print(x)

if __name__ == "__main__":
    main()
