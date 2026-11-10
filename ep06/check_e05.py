text = open("../data/proverbs.txt", encoding="utf-8").read()
train = text[:int(0.9 * len(text))]
chars = sorted(set(text))
N = {a: {b: 0 for b in chars} for a in chars}
for a, b in zip(train, train[1:]):
    N[a][b] += 1
row = [N["e"][b] for b in chars]
total = sum(row)
probs = [n / total for n in row]
for b, p in zip(chars, probs):
    if p > 0.07:
        print(repr(b), round(p, 2))
tot_t = sum(N["t"].values())
print("after e:", N["e"][" "], "/", total, "=", round(N["e"][" "] / total, 2))
print("after t:", N["t"][" "], "/", tot_t, "=", round(N["t"][" "] / tot_t, 2))
