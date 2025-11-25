from pprint import pprint

d = {"a":1, "b":2, "c":3}
filter = {k: v for k, v in d.items() if v > 1}
print(filter)

e = {"a":list(range(1,10)),
     "b":list(range(10,20)),
     "c":list(range(20,30))}
pprint(e)



