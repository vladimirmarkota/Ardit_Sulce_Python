dictionary = {"a": 1, "b": 2}
dictionary2 = dict(a=1, b=2)
print(dictionary)
print(dictionary2)

print(dictionary["b"])

d = {"a": 1, "b": 2, "c": 3}
print(d["a"] + d["b"])

d["d"] = 4
print(d)

zbroj = 0
for i in d:
    zbroj += d[i]

print(zbroj)

e = d.values()
print(sum(e))

print(sum(d.values()))
