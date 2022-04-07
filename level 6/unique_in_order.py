def unique_in_order(iterable):
    res = []
    if len(iterable) != 0:
        res.append(iterable[0])
        for x in range(len(iterable) - 1):
            if iterable[x] != iterable[x + 1]:
                res.append(iterable[x + 1])

    else:
        res = []

    return res


print(unique_in_order(input()))
