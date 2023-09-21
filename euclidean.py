import math


state = [7, 2, 4, 5, 0, 6, 8, 3, 1]

result = 0

for i in range(9):
    if state[i]!=0:
        y = state[i]//3 - i//3
        x = state[i]%3 - i%3
        print(x**2 + y**2)
        result += math.sqrt(x**2 + y**2)

print("Euclidean:", result)