text = open("../data/proverbs.txt", encoding="utf-8").read()
stoi = {ch: i for i, ch in enumerate(sorted(set(text)))}
data = [stoi[c] for c in text]
n = int(0.9 * len(data))
train, val = data[:n], data[n:]
print(len(data), n)
print(len(train), len(val))
print(text[n:])
