text = open("../data/proverbs.txt", encoding="utf-8").read()
train = text[:int(0.9 * len(text))]
chars = sorted(set(text))
N = {a: {b: 0 for b in chars} for a in chars}
for a, b in zip(train, train[1:]):
    N[a][b] += 1
print(N["t"]["h"], N["h"]["t"])
print(sum(N["t"].values()))
