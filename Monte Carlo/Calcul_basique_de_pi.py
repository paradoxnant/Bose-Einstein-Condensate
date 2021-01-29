import random

essaie = 4000
tirs = 0
for iter in range(essaie):
    x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
    if x**2 + y**2 < 1.0: 
        tirs += 1
print (4.0 * tirs / float(essaie))
