# E11: The Bigram Model as a Neural Network

Playlist: https://www.youtube.com/playlist?list=PLNEAUFhep8gE

## Setup

This episode needs PyTorch, as in E07 to E10. Run every script from inside this folder; they read the shared dataset at `../data/proverbs.txt`.

```
cd ep11
python check_e10.py
python examples.py
python softmax.py
python forward.py
python train.py
python compare.py
```

- `check_e10.py`: checks the E10 "your turn", in PyTorch (the same numbers we already matched to our `Value` class in E10). Starting the one-knob model at w = 6.0 gives `w.grad = 24.0` and `diff.grad = 12.0`. In the neuron, setting x2 to 0.0 makes `w2.grad = 0.0`, because w2 is multiplied by zero, so nudging it cannot change the output. The output is 0.7163, and `w1.grad = b.grad = 0.4869`.
- `examples.py`: the same 90% training split as before, 27 characters and 705 neighbour pairs. The first proverb starts "the monkey...", so the first pairs are t→h, h→e, e→space, space→m, m→o. Each pair is one quiz: "I just saw this; what comes next?"
- `softmax.py`: three raw scores, 2.0, 1.0 and 0.0. Raising e to each score gives 7.389, 2.718 and 1.000, which add to 11.107. `F.softmax` turns them into chances 0.665, 0.245 and 0.090, which add to 1.0. A score of zero still gets a share; nothing is stuck at zero.
- `forward.py`: a 27×27 grid of random knobs `W = torch.randn(V, V, requires_grad=True)`, `logits = xenc @ W`, then softmax and `F.cross_entropy`. With seed 27, the first pair t→h has logit −0.33 and chance 0.0174. The loss on all 705 pairs is 3.71, a little worse than a fair guess of log(27) ≈ 3.30.
- `train.py`: two hundred steps of gradient descent, `loss.backward()` then `W.data -= lr * W.grad`, with learning rate 50. The loss falls 3.71, 2.10, 2.06, 2.05 (steps 0, 50, 100, 200). Most of the drop is in the first fifty steps.
- `compare.py`: trains the same network, then stands it next to the counting model from episodes 4 to 6. Training loss: counting 2.04, neural 2.05. Validation: counting with add-one smoothing 2.57, neural 2.53 (the network never outputs an exact zero, a bit like smoothing, learned by itself). After t, both models give a space a chance of 0.28 and h a chance of 0.36.

Our real run is saved next to each script (`.txt`). Versions: Python 3.13, PyTorch 2.15.0 (CPU build).
