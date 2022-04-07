def string_clean(s):
    """
    Function will return the cleaned string
    """
    res = ''
    for i in s:
        if i.isdigit():
            continue
        res += i
    return res


test1 = string_clean('! !')
test2 = string_clean('123456789')
test3 = string_clean('This looks5 grea8t!')

print(test1)
print(test2)
print(test3)