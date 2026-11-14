import torch
import torch.nn.functional as F
text = open("../data/proverbs.txt", encoding="utf-8").read()
train = text[:int(0.9 * len(text))]
chars = sorted(set(text))
stoi = {ch: i for i, ch in enumerate(chars)}
V = len(chars)
N = torch.zeros((V, V), dtype=torch.int32)
for a, b in zip(train, train[1:]):
    N[stoi[a], stoi[b]] += 1
print("shape:", N.shape)
t = stoi["t"]
print("row t total:", N[t].sum().item())
print("t then h:", N[t, stoi["h"]].item())
x = F.one_hot(torch.tensor(t), num_classes=V).float()
row = x @ N.float()
print("same as row t:", torch.equal(row, N[t].float()))
