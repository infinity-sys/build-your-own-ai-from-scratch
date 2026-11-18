x = 2.0
target = 6.0

def mistake(w):
    prediction = w * x
    return (prediction - target) ** 2

for w in [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]:
    print("w =", w, "  mistake =", mistake(w))
