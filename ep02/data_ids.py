text = open("../data/proverbs.txt", encoding="utf-8").read()
stoi = {ch: i for i, ch in enumerate(sorted(set(text)))}
data = [stoi[c] for c in text]
print(len(data))
print(text.splitlines()[0])
print(data[:45])
