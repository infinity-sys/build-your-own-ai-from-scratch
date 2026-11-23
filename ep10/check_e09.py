x = 2.0
target = 6.0

def mistake(w):
    return (w * x - target) ** 2

def slope(f, w, h=0.0001):
    return (f(w + h) - f(w)) / h

def descend(w, lr):
    print("start =", w, " lr =", lr, " first slope:", round(slope(mistake, w)))
    path = []
    for step in range(10):
        w = w - lr * slope(mistake, w)
        path.append(round(w, 3))
    print("  w:", path[:4], "... after 10 steps:", path[-1])

descend(6.0, 0.05)
descend(0.0, 0.25)
