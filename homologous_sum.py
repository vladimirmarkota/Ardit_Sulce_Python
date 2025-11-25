a = [1, 2, 3]
b = (4, 5, 6)

i = 0
while i < len(a):
    print(a[i] + b[i])
    i += 1

for i, j in zip(a, b):
    print(i + j)




