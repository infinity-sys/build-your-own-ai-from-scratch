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
logits = xenc @ W
# first pair is t -> h
h = stoi["h"]
print("logit for h after t:", round(logits[0, h].item(), 2))
probs = F.softmax(logits[0], dim=0)
print("chance of h after t:", round(probs[h].item(), 4))
loss = F.cross_entropy(logits, ys)
print("loss on all 705 pairs:", round(loss.item(), 2))
