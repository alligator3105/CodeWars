def powers_of_two(n):
    return [2**x for x in range(n+1)]


res = powers_of_two(int(input()))
print(res)