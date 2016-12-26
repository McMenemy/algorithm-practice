def urlify(string):
    return '%20'.join(string.split())

print(urlify("Mr John Smith") == "Mr%20John%20Smith")
