import torch

x = torch.tensor([1.0, 0.5])
w = torch.tensor([0.8, -0.4], requires_grad=True)
b = torch.tensor(0.1, requires_grad=True)
out = torch.tanh(x @ w + b)
out.backward()
print("output: ", round(out.item(), 4))
print("w1.grad:", round(w.grad[0].item(), 4))
print("w2.grad:", round(w.grad[1].item(), 4))
print("b.grad: ", round(b.grad.item(), 4))
