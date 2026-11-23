from value import Value

x = Value(2.0)
w = Value(0.0)
prediction = w * x
diff = prediction + Value(-6.0)
mistake = diff * diff
print("mistake:", mistake.data)

mistake.backward()
print("w.grad:", w.grad)
print("diff.grad:", diff.grad)
