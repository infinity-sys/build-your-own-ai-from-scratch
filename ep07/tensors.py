import torch
s = torch.tensor(5.0)
v = torch.tensor([2.0, 0.0, 1.0])
M = torch.zeros(2, 3)
B = torch.zeros(4, 2, 3)
for name, t in [("s", s), ("v", v), ("M", M), ("B", B)]:
    print(name, "shape:", tuple(t.shape), "dims:", t.ndim, "numbers:", t.numel())
