def cw(filepath):
    with open(filepath) as file:
        content = file.read()
        content1 = content.replace(",", " ")
        words = content1.split()
        return len(words)

print(cw("words2.txt"))
