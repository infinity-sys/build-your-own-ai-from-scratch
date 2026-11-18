x = 2.0
target = 6.0

def mistake(w):
    return (w * x - target) ** 2

def slope(f, w, h=0.0001):
    return (f(w + h) - f(w)) / h

for lr in [0.01, 0.05, 0.3]:
    w = 0.0
    for step in range(10):
        w = w - lr * slope(mistake, w)
    print("lr =", lr, "  w after 10 steps =", round(w, 2), "  mistake =", round(mistake(w), 2))
