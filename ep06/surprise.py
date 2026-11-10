import math
for p in [1.0, 0.5, 0.36, 0.28, 0.09, 0.01]:
    print(p, round(max(0.0, -math.log(p)), 2))
