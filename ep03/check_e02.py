text = open("../data/proverbs.txt", encoding="utf-8").read()
stoi = {ch: i for i, ch in enumerate(sorted(set(text)))}
print([stoi[c] for c in "friend"])
mine = "just enjoy a quiet evening"
print(sorted(set(c for c in mine if c not in stoi)))
