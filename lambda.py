n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))
print(n(0))
print(n(-3))

x = lambda x: x * 3 if x > 0 else "Ne moze"
print(x(0))
print(x(1))
print(x(2))

listic = [lambda arg=x: arg * 10 for x in range(1,5)]
for i in listic:
    print(i())

r = range(1, 21)
r2 = list(map(lambda x: x * 2, r))
print(r2)

