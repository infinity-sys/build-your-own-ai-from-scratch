x = 2.0
target = 6.0

def mistake(w):
    return (w * x - target) ** 2

def slope(f, w, h=0.0001):
    return (f(w + h) - f(w)) / h

for w in [1.0, 3.0, 5.0]:
    print("w =", w, "  slope =", round(slope(mistake, w), 2))
