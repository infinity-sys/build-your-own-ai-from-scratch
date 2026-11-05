text = open("../data/proverbs.txt", encoding="utf-8").read()
chars = sorted(set(text))
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for ch, i in stoi.items()}

def encode(s):
    return [stoi[c] for c in s]

def decode(ids):
    return "".join(itos[i] for i in ids)

ids = encode("patience")
print(ids)
print(decode(ids))
print(decode(encode(text)) == text)
