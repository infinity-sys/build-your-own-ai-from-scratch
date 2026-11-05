text = open("../data/proverbs.txt", encoding="utf-8").read()
train = text[:int(0.9 * len(text))]
chars = sorted(set(text))
N = {a: {b: 0 for b in chars} for a in chars}
for a, b in zip(train, train[1:]):
    N[a][b] += 1
row = [N["t"][b] for b in chars]
probs = [n / sum(row) for n in row]
for b, p in zip(chars, probs):
    if p > 0.06:
        print(repr(b), round(p, 2))
print("total:", round(sum(probs), 2))
