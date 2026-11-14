# E07: Numbers in Grids: Vectors, Matrices and Tensors with PyTorch

Playlist: https://www.youtube.com/playlist?list=PLNEAUFhep8gE

## Setup (once)

This is the first episode that needs a package: PyTorch. Inside the course's virtual environment (see the main README):

```
pip install -r requirements.txt   # installs torch 2.15.0
```

or simply `pip install torch`. The download is a few hundred MB.

- macOS (Apple silicon or Intel) and Windows: `pip install torch` installs the normal build.
- Linux without an NVIDIA graphics card: `pip install torch --index-url https://download.pytorch.org/whl/cpu` gives a much smaller CPU-only build.

You do not need a graphics card (GPU) for this course: our models are tiny.

## This episode

```
cd ep07
python check_e06.py
python hello_torch.py
python vectors.py
python matrices.py
python tensors.py
python matmul.py
python onehot.py
python bigram_tensor.py
```

- `check_e06.py`: checks the E06 "your turn": add-two smoothing, `p = (count + 2) / (total + 2 * V)`. Training loss 2.55, validation loss 2.69: both go up (add-one gave 2.39 and 2.57). A little smoothing helps; too much hurts.
- `hello_torch.py`: prints the PyTorch version and a first tensor, `tensor([1, 2, 3])`. Our run shows `2.15.0+cpu` (the CPU-only build); yours may show `2.15.0` or a newer version.
- `vectors.py`: a vector is a list of numbers. `torch.tensor([2.0, 0.0, 1.0])` has shape `[3]`; `v[0]` is a scalar tensor; `v * 10` and `v + v` work element by element, no loop.
- `matrices.py`: a matrix is a grid, rows first. Shape `[2, 3]`; `M[1]` is a row, `M[1, 2]` is 6, `M[:, 0]` is column 0.
- `tensors.py`: tensor is the general name. Shapes `()`, `(3,)`, `(2, 3)`, `(4, 2, 3)` have 0, 1, 2, 3 dimensions (`ndim`) and hold 1, 3, 6, 24 numbers (`numel()`).
- `matmul.py`: vector times matrix with `@`. `[1, 0, 2] @ [[1, 2], [3, 4], [5, 6]]` is `[11, 14]`: multiply the pairs down each column, then add. Shapes: `(3) @ (3, 2)` gives `(2)`; the middle sizes must match.
- `onehot.py`: `F.one_hot` turns the ID of `t` (20) into 27 zeros with a single 1 at index 20 (whole numbers, `int64`). A one-hot vector times a matrix picks one row: `one_hot(1, 3).float() @ W` is `[3, 4]`.
- `bigram_tensor.py`: our bigram counting table as a 27 by 27 tensor (`torch.int32`). Row `t` adds up to 58, `t` then `h` is 21 (21 / 58 = 0.36), and one-hot(t) `@` N gives back row `t` exactly (`True`).

Run every script from inside `ep07/`; `check_e06.py`, `onehot.py` and `bigram_tensor.py` read `../data/proverbs.txt`. Our real run is saved next to each script (`.txt`). Versions: Python 3.13, PyTorch 2.15.0 (CPU build).
