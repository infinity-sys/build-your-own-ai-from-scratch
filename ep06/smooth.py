import math
text = open("../data/proverbs.txt", encoding="utf-8").read()
n = int(0.9 * len(text))
train, val = text[:n], text[n:]
chars = sorted(set(text))
N = {a: {b: 0 for b in chars} for a in chars}
for a, b in zip(train, train[1:]):
    N[a][b] += 1
V = len(chars)
def loss(part):
    nlls = []
    for a, b in zip(part, part[1:]):
        p = (N[a][b] + 1) / (sum(N[a].values()) + V)
        nlls.append(-math.log(p))
    return sum(nlls) / len(nlls)
print("train:", round(loss(train), 2))
print("val:", round(loss(val), 2))
