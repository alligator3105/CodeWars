def stringy(size):
    res = ''
    for x in range(size):
        if x % 2 == 0:
            res += '1'
        else:
            res += '0'

    return res


test1 = stringy(3)
test2 = stringy(1)
test3 = stringy(54)

print(test1)
print(test2)
print(test3)
