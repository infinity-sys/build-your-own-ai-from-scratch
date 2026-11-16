import math
x1, x2 = 1.0, 0.5
w2, b = -0.4, 0.1
for w1 in [-1.0, -0.5, 0.0, 0.5, 1.0]:
    out = math.tanh(w1 * x1 + w2 * x2 + b)
    print("w1 =", w1, "  output =", round(out, 2))
