import torch
import torch.nn.functional as F

scores = torch.tensor([2.0, 1.0, 0.0])
print("scores:", scores.tolist())
exps = scores.exp()
print("exp(scores):", ", ".join(f"{v:.3f}" for v in exps.tolist()))
print("sum of exp:", f"{exps.sum().item():.3f}")
probs = F.softmax(scores, dim=0)
print("softmax:", ", ".join(f"{v:.3f}" for v in probs.tolist()))
print("sum of softmax:", f"{probs.sum().item():.3f}")
