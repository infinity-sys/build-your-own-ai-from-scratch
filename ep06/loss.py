import math
text = open("../data/proverbs.txt", encoding="utf-8").read()
train = text[:int(0.9 * len(text))]
chars = sorted(set(text))
N = {a: {b: 0 for b in chars} for a in chars}
for a, b in zip(train, train[1:]):
    N[a][b] += 1
nlls = []
for a, b in zip(train, train[1:]):
    p = N[a][b] / sum(N[a].values())
    nlls.append(-math.log(p))
print("pairs:", len(nlls))
print("loss:", round(sum(nlls) / len(nlls), 2))
