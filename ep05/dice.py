import random
random.seed(1)
sides = ["h", " ", "o"]
weights = [21, 16, 5]
rolls = random.choices(sides, weights=weights, k=20)
print(rolls)
print(rolls.count("h"), rolls.count(" "), rolls.count("o"))
