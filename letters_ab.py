import string

with open("letters.txt", "w") as f:
    for l1, l2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
        f.write(l1 + l2 + "\n")

print(f)

