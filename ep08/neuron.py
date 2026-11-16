import math
x1, x2 = 1.0, 0.5
w1, w2 = 0.8, -0.4
b = 0.1
z = w1 * x1 + w2 * x2 + b
out = math.tanh(z)
print("weighted sum z:", round(z, 2))
print("output:", round(out, 2))
