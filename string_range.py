def puta(val):
    return val * 2

my_range = range(1, 21)

res = map(str, my_range)
print(list(res))

kk = map(puta, my_range)
print(list(kk))






