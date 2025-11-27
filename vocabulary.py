d = dict(weather = "clima", earth = "terra", rain = "chuva")

word = input("Enter a word: ").lower()

def vocabulary(word):
    try:
        return d[word].lower()
    except KeyError:
        return "We couldn't find that word!"

print(vocabulary(word))
