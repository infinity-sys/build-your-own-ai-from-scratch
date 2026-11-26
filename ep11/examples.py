text = open("../data/proverbs.txt", encoding="utf-8").read()
train = text[:int(0.9 * len(text))]
chars = sorted(set(text))
stoi = {ch: i for i, ch in enumerate(chars)}
print("characters:", len(chars))
pairs = list(zip(train, train[1:]))
print("train pairs:", len(pairs))
print("first five:")
for a, b in pairs[:5]:
    print(repr(a), "->", repr(b), "ids", stoi[a], stoi[b])
