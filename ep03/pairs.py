text = open("../data/proverbs.txt", encoding="utf-8").read()
counts = {}
for a, b in zip(text, text[1:]):
    counts[a + b] = counts.get(a + b, 0) + 1
top = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
print(top[:5])
