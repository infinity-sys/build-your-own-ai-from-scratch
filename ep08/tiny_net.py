import torch
x = torch.tensor([1.0, 0.5])
W1 = torch.tensor([[0.5, -1.0, 0.2],
                   [1.0, 0.4, -0.6]])
b1 = torch.tensor([0.0, 0.3, 0.2])
W2 = torch.tensor([1.0, -0.5, 2.0])
b2 = torch.tensor(-0.4)
h = torch.tanh(x @ W1 + b1)
out = torch.tanh(h @ W2 + b2)
print("hidden h:", [round(v, 2) for v in h.tolist()])
print("output:", round(out.item(), 2))
print("knobs:", W1.numel() + b1.numel() + W2.numel() + b2.numel())
