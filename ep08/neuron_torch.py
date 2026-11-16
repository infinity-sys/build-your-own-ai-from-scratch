import torch
x = torch.tensor([1.0, 0.5])
w = torch.tensor([0.8, -0.4])
b = torch.tensor(0.1)
z = x @ w + b
out = torch.tanh(z)
print("z:", round(z.item(), 2))
print("output:", round(out.item(), 2))
