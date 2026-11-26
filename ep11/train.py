import torch
import torch.nn.functional as F

text = open("../data/proverbs.txt", encoding="utf-8").read()
train = text[:int(0.9 * len(text))]
chars = sorted(set(text))
stoi = {ch: i for i, ch in enumerate(chars)}
V = len(chars)
xs, ys = [], []
for a, b in zip(train, train[1:]):
    xs.append(stoi[a])
    ys.append(stoi[b])
xs, ys = torch.tensor(xs), torch.tensor(ys)
xenc = F.one_hot(xs, num_classes=V).float()

torch.manual_seed(27)
W = torch.randn(V, V, requires_grad=True)
lr = 50
for step in range(200):
    logits = xenc @ W
    loss = F.cross_entropy(logits, ys)
    if step in (0, 50, 100):
        print("step", step, "loss", f"{loss.item():.2f}")
    W.grad = None
    loss.backward()
    W.data -= lr * W.grad
loss = F.cross_entropy(xenc @ W, ys)
print("step", 200, "loss", f"{loss.item():.2f}")
