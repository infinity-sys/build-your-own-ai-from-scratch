text = open("../data/proverbs.txt", encoding="utf-8").read()
words = text.split()
print(len(words), len(set(words)))
print(words[:9])
