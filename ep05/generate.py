import random
text = open("../data/proverbs.txt", encoding="utf-8").read()
train = text[:int(0.9 * len(text))]
chars = sorted(set(text))
N = {a: {b: 0 for b in chars} for a in chars}
for a, b in zip(train, train[1:]):
    N[a][b] += 1
def probs(a):
    row = [N[a][b] for b in chars]
    return [n / sum(row) for n in row]
random.seed(27)
for i in range(5):
    out = ""
    ch = random.choices(chars, weights=probs("\n"))[0]
    while ch != "\n":
        out += ch
        ch = random.choices(chars, weights=probs(ch))[0]
    print(out)
