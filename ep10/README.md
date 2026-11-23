# E10: Backpropagation, Step by Step

Playlist: https://www.youtube.com/playlist?list=PLNEAUFhep8gE

## Setup

Nothing new to install. Every script uses plain Python, except `neuron_torch.py`, which needs PyTorch (as in E07 and E08). Run the scripts from inside this folder, so that `from value import Value` finds `value.py`.

## This episode

```
cd ep10
python check_e09.py
python chain.py
python one_knob_value.py
python neuron_value.py
python neuron_torch.py
```

- `check_e09.py`: checks the E09 "your turn". Starting at w = 6.0, the first slope is +24, so w moves left: 4.8, 4.08, 3.648, ... 3.018 after 10 steps. With a learning rate of 0.25 from w = 0, every step is exactly 6, so w bounces 6, 0, 6, 0, ... forever.
- `chain.py`: the chain rule by hand for the one-knob model (x = 2, target = 6, w = 0). Forward: prediction 0.0, diff -6.0, mistake 36.0. Backward, one "runner" per line (local slope × the blame it receives): 1.0, -12.0, -12.0, -24.0. The -24 is the same slope E09 found by nudging.
- `value.py`: our tiny autograd engine, the class `Value`. Each Value keeps its `data`, its `grad`, its `children` and a `backward_step` rule. `__add__` (local slope 1), `__mul__` (local slope = the other number) and `tanh` (local slope 1 - t²) each attach their rule; grads use `+=` so a Value used twice (like `diff * diff`) collects blame from both uses. `backward()` builds a topological order (children first) and runs every rule once, in reverse, starting from grad 1.0.
- `one_knob_value.py`: the one-knob model with Values. `mistake.backward()` gives `w.grad = -24.0` and `diff.grad = -12.0`, with no backward lines written by hand.
- `neuron_value.py`: the E08 neuron (inputs 1.0 and 0.5, weights 0.8 and -0.4, bias 0.1) with Values: output 0.6044, grads 0.6347, 0.3174, 0.6347.
- `neuron_torch.py`: the same neuron in PyTorch with `requires_grad=True` and `out.backward()`: the same four numbers.

Our `Value` class is a simplified version of Andrej Karpathy's micrograd: https://github.com/karpathy/micrograd

Our real run is saved next to each script (`.txt`). Versions: Python 3.13, PyTorch 2.15.0 (CPU build, only for `neuron_torch.py`).
