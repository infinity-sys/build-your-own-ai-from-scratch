import torch
M = torch.tensor([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0]])
print(M)
print(M.shape)
print(M[1])
print(M[1, 2])
print(M[:, 0])
