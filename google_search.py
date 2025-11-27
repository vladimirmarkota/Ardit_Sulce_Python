import webbrowser

query = input("What would you like to search for?")
webbrowser.open("https://google.com/search?q=%s" % query)
