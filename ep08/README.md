# E08: What Is a Neuron? A Tiny Network, Forward Pass

Watch: https://youtu.be/nFMj24BjAXo
Playlist: https://www.youtube.com/playlist?list=PLNEAUFhep8gE

## Setup

Same as E07: PyTorch inside the course's virtual environment (`pip install -r requirements.txt`, torch 2.15.0). `neuron.py`, `knobs.py` and `squash.py` need only Python's built-in `math`.

## This episode

```
cd ep08
python check_e07.py
python neuron.py
python knobs.py
python squash.py
python neuron_torch.py
python tiny_net.py
```

- `check_e07.py`: checks the E07 "your turn". `[1, 0, 2] @ torch.ones(3, 4)` is `tensor([3., 3., 3., 3.])` with shape `[4]` (each output is 1 + 0 + 2). `torch.ones(2, 4)` fails with `RuntimeError: mm: mat1 and mat2 shapes cannot be multiplied (1x3 and 2x4)`: x has 3 numbers but W has only 2 rows, so the middle sizes do not match.
- `neuron.py`: one neuron in plain Python. Inputs `x1, x2 = 1.0, 0.5`, weights `w1, w2 = 0.8, -0.4`, bias `b = 0.1`. Step 1, the weighted sum: `z = w1 * x1 + w2 * x2 + b` = 0.7. Step 2, the squash: `out = math.tanh(z)` = 0.6.
- `knobs.py`: weights are knobs. Turning `w1` from -1 to +1 (everything else fixed) moves the output from -0.8 through -0.54, -0.1, 0.38 to 0.72. Learning means turning the knobs until the outputs are right.
- `squash.py`: `tanh` squashes any number into the range -1 to +1: -3 gives -1.0, 0 stays 0, 0.7 gives 0.6, 3 and 10 both give 1.0.
- `neuron_torch.py`: the same neuron with tensors. The weighted sum is a vector multiplication: `z = x @ w + b`, then `torch.tanh(z)`. Same answer: 0.7 and 0.6.
- `tiny_net.py`: a tiny network with 2 inputs, a hidden layer of 3 neurons and 1 output neuron. The forward pass is two lines: `h = torch.tanh(x @ W1 + b1)` (shapes `(2) @ (2, 3)` gives `(3)`) and `out = torch.tanh(h @ W2 + b2)`. Hidden values `[0.76, -0.46, 0.1]`, output 0.66, and 13 knobs (6 + 3 + 3 + 1). The knobs were chosen by hand; learning them starts in E09.

Our real run is saved next to each script (`.txt`). Versions: Python 3.13, PyTorch 2.15.0 (CPU build).
