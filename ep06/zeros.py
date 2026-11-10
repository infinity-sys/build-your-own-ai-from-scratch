text = open("../data/proverbs.txt", encoding="utf-8").read()
n = int(0.9 * len(text))
train, val = text[:n], text[n:]
chars = sorted(set(text))
N = {a: {b: 0 for b in chars} for a in chars}
for a, b in zip(train, train[1:]):
    N[a][b] += 1
zeros = 0
for a, b in zip(val, val[1:]):
    p = N[a][b] / sum(N[a].values())
    if p == 0:
        print(repr(a), "->", repr(b))
        zeros += 1
print("zero pairs:", zeros)
