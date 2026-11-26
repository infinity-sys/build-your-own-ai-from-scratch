import math
import torch
import torch.nn.functional as F

text = open("../data/proverbs.txt", encoding="utf-8").read()
n = int(0.9 * len(text))
train, val = text[:n], text[n:]
chars = sorted(set(text))
stoi = {ch: i for i, ch in enumerate(chars)}
V = len(chars)
xs, ys = [], []
for a, b in zip(train, train[1:]):
    xs.append(stoi[a])
    ys.append(stoi[b])
xs, ys = torch.tensor(xs), torch.tensor(ys)
xenc = F.one_hot(xs, num_classes=V).float()

N = torch.zeros((V, V))
for a, b in zip(xs, ys):
    N[a, b] += 1

def count_loss(part, add=0):
    nlls = []
    for a, b in zip(part, part[1:]):
        row = N[stoi[a]]
        p = (row[stoi[b]] + add) / (row.sum() + add * V)
        nlls.append(-math.log(p.item()))
    return sum(nlls) / len(nlls)

torch.manual_seed(27)
W = torch.randn(V, V, requires_grad=True)
lr = 50
for step in range(200):
    loss = F.cross_entropy(xenc @ W, ys)
    W.grad = None
    loss.backward()
    W.data -= lr * W.grad

vx, vy = [], []
for a, b in zip(val, val[1:]):
    vx.append(stoi[a])
    vy.append(stoi[b])
vx, vy = torch.tensor(vx), torch.tensor(vy)
nloss = F.cross_entropy(xenc @ W, ys)
vX = F.one_hot(vx, V).float()
vloss = F.cross_entropy(vX @ W, vy)
print("counting train:", f"{count_loss(train):.2f}")
print("neural train:  ", f"{nloss.item():.2f}")
print("counting val +1:", f"{count_loss(val, 1):.2f}")
print("neural val:    ", f"{vloss.item():.2f}")
t, spc, h = stoi["t"], stoi[" "], stoi["h"]
cp = N[t] / N[t].sum()
np_ = F.softmax(W[t], dim=0)
print("after t, chance of space:")
print("  counting:", round(cp[spc].item(), 2))
print("  neural:  ", round(np_[spc].item(), 2))
print("after t, chance of h:")
print("  counting:", round(cp[h].item(), 2))
print("  neural:  ", round(np_[h].item(), 2))
