import random
import math

n = int(input('試行回数の代入：'))
x = 0

for i in range(n+1):
    a = random.random()
    b = random.random()
    c = math.sqrt(a ** 2 + b ** 2)

    if c <= 1:
        x += 1

pi = 4 * x / n
print(pi)

