import torch
x = torch.tensor([1.0, 0.0, 2.0])
W = torch.tensor([[1.0, 2.0],
                  [3.0, 4.0],
                  [5.0, 6.0]])
print(x.shape, W.shape)
y = x @ W
print(y)
print(y.shape)
first = x[0] * W[0, 0] + x[1] * W[1, 0] + x[2] * W[2, 0]
print(first)
