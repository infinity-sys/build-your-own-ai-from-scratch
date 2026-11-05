text = open("../data/proverbs.txt", encoding="utf-8").read()
chars = sorted(set(text))
print(len(chars))
print(chars)
