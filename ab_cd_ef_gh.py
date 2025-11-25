import string

list = string.ascii_lowercase
print(list)

a = list[0::2]
b = list[1::2]

print(b)
print(a)

for i, j in zip(a, b):
    print(i + j)

