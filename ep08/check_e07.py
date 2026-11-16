import torch
x = torch.tensor([1.0, 0.0, 2.0])
W = torch.ones(3, 4)
y = x @ W
print(y)
print(y.shape)
try:
    print(x @ torch.ones(2, 4))
except RuntimeError as e:
    print("RuntimeError:", e)
