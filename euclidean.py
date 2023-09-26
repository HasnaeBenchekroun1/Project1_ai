import math


state = [7, 2, 4, 5, 0, 6, 8, 3, 1]

result = 0
col = 0
row = 0

for i in range(9):
    if state[i]!=0:
        y = abs(state[i]//3 - i//3)
        if(y!=0):
            result+=1
        x = abs(state[i]%3 - i%3)
        if(x!=0):
            result+=1
        print(row + col)


print("Euclidean:", result)