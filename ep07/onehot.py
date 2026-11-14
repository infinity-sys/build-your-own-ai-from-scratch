import torch
import torch.nn.functional as F
text = open("../data/proverbs.txt", encoding="utf-8").read()
chars = sorted(set(text))
stoi = {ch: i for i, ch in enumerate(chars)}
ix = torch.tensor(stoi["t"])
x = F.one_hot(ix, num_classes=len(chars))
print("id of t:", ix.item())
print(x)
print(x.shape, x.dtype)
W = torch.tensor([[1.0, 2.0],
                  [3.0, 4.0],
                  [5.0, 6.0]])
print(F.one_hot(torch.tensor(1), num_classes=3).float() @ W)
