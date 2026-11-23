# E09: Learning from Mistakes: Slopes and Gradient Descent

Watch: https://youtu.be/WbsoLi2C2t4

Playlist: https://www.youtube.com/playlist?list=PLNEAUFhep8gE

## Setup

Nothing new to install: every script in this episode uses plain Python (`check_e08.py` needs PyTorch, as in E07 and E08).

## This episode

```
cd ep09
python check_e08.py
python mistake.py
python slope.py
python descent.py
python learning_rate.py
```

- `check_e08.py`: checks the E08 "your turn". `tiny_net.py` with `x = [0.0, 1.0]` gives hidden values `[0.76, 0.6, -0.38]` and output -0.6 (negative): only the second row of `W1` matters, its -0.6 pulls the third hidden neuron down, and `W2` gives that neuron the biggest weight, 2.0.
- `mistake.py`: a one-knob model, `prediction = w * x` with `x = 2.0` and `target = 6.0`. The mistake (loss) is `(prediction - target) ** 2`. For w = 0..5 it is 36, 16, 4, 0, 4, 16: a valley with its bottom at w = 3.
- `slope.py`: the numerical slope `(f(w + h) - f(w)) / h` with a tiny nudge `h = 0.0001`. Slopes: -16 at w = 1 (downhill to the right), 0 at w = 3 (the bottom), +16 at w = 5 (uphill to the right).
- `descent.py`: gradient descent, `w = w - lr * slope(mistake, w)`, from w = 0 with learning rate 0.05. After 10 steps w = 2.982 and the mistake is 0.0013: it finds w = 3 by itself.
- `learning_rate.py`: the same 10 steps with three learning rates. 0.01 is too slow (w = 1.7), 0.05 is about right (w = 2.98), 0.3 jumps over the bottom and explodes (w = -83.78, mistake 30119.6).

Our real run is saved next to each script (`.txt`). Versions: Python 3.13, PyTorch 2.15.0 (CPU build, only for `check_e08.py`).
