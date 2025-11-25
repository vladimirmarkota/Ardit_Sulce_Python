from idlelib.browser import file_open


def count_words_in_file(filepath):
    with open(filepath, "r") as file:
        content = file.read()
    items = content.split()
    return len(items)

print(count_words_in_file("words1.txt"))
