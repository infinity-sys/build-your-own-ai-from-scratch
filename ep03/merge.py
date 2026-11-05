text = open("../data/proverbs.txt", encoding="utf-8").read()
tokens = list(text)
print(len(tokens))
merged, i = [], 0
while i < len(tokens):
    if tokens[i:i + 2] == ["e", " "]:
        merged.append("e ")
        i += 2
    else:
        merged.append(tokens[i])
        i += 1
print(len(merged))
print(merged[:12])
