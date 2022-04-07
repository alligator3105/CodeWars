def filter_list(l):
    a = filter(lambda x: type(x) is int, l)
    res = list(a)
    return res


dis = filter_list([1, 2, 'aasf', '1', '123', 123])
print(dis)