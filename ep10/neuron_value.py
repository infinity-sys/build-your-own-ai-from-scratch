from value import Value

x1, x2 = Value(1.0), Value(0.5)
w1, w2 = Value(0.8), Value(-0.4)
b = Value(0.1)
z = w1 * x1 + w2 * x2 + b
out = z.tanh()
out.backward()
print("output: ", round(out.data, 4))
print("w1.grad:", round(w1.grad, 4))
print("w2.grad:", round(w2.grad, 4))
print("b.grad: ", round(b.grad, 4))
