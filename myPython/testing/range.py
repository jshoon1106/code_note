import random

rand = [i for i in range(6)]
for i in range(6):
    rand[i] = random.randint(1, 9)
    for j in range(i):
        if rand[j] == rand[i]:
            rand[i] = random.randint(1, 9)
            j = 0
print(rand)