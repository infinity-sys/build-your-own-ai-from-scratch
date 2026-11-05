text = open("../data/proverbs.txt", encoding="utf-8").read()
stoi = {ch: i for i, ch in enumerate(sorted(set(text)))}
try:
    print([stoi[c] for c in "joy"])
except KeyError as e:
    print("unknown character:", e)
