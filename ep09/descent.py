x = 2.0
target = 6.0

def mistake(w):
    return (w * x - target) ** 2

def slope(f, w, h=0.0001):
    return (f(w + h) - f(w)) / h

w = 0.0
lr = 0.05
for step in range(10):
    w = w - lr * slope(mistake, w)
    print("step", step + 1, "  w =", round(w, 3), "  mistake =", round(mistake(w), 4))
