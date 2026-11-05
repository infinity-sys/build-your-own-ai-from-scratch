text = open("../data/proverbs.txt", encoding="utf-8").read()
tokens = list(text)
merged, i = [], 0
while i < len(tokens):
    if tokens[i:i + 2] == ["s", " "]:
        merged.append("s ")
        i += 2
    else:
        merged.append(tokens[i])
        i += 1
print(len(tokens), len(merged), len(tokens) - len(merged))
