def likes(names):
    display = ''
    if len(names) == 0:
        display = "no one likes this"
    elif len(names) == 1:
        display = names[0] + ' likes this'
    elif len(names) == 2:
        display = names[0] + ' and ' + names[1] + ' likes this'
    elif len(names) == 3:
        display = names[0] + ', ' + names[1] + ' and ' + names[2] + ' likes this'
    else:
        display = names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this'

    return display


res = likes(input().split())
print(res)
