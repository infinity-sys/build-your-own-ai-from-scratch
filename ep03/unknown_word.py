text = open("../data/proverbs.txt", encoding="utf-8").read()
words = set(text.split())
chars = set(text)
new = "patiently"
print(new in words)
print(all(c in chars for c in new))
