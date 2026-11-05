import json
text = open("../data/proverbs.txt", encoding="utf-8").read()
train = text[:int(0.9 * len(text))]
chars = sorted(set(text))
N = {a: {b: 0 for b in chars} for a in chars}
for a, b in zip(train, train[1:]):
    N[a][b] += 1
m = [[N[a][b] for b in chars] for a in chars]
json.dump({"labels": chars, "m": m}, open("heat.json", "w"))
zeros = sum(row.count(0) for row in m)
print(len(m), "x", len(m[0]), "=", len(m) * len(m[0]), "cells")
print(zeros, "cells are zero")
