import torch

# 1) one-knob model, start at w = 6.0
x = torch.tensor(2.0)
w = torch.tensor(6.0, requires_grad=True)
prediction = w * x
diff = prediction - 6.0
diff.retain_grad()
mistake = diff * diff
print("mistake:", mistake.item())
mistake.backward()
print("w.grad:", w.grad.item())
print("diff.grad:", diff.grad.item())

# 2) neuron, x2 = 0.0
x1 = torch.tensor(1.0)
x2 = torch.tensor(0.0)
w1 = torch.tensor(0.8, requires_grad=True)
w2 = torch.tensor(-0.4, requires_grad=True)
b = torch.tensor(0.1, requires_grad=True)
out = torch.tanh(w1 * x1 + w2 * x2 + b)
out.backward()
print("output: ", round(out.item(), 4))
print("w1.grad:", round(w1.grad.item(), 4))
print("w2.grad:", round(w2.grad.item(), 4))
print("b.grad: ", round(b.grad.item(), 4))
