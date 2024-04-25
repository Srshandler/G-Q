import random

NUM = 10000
v = []
for i in range(NUM):
  v.append(random.randint(0, NUM))

s = 15

def stsum(v, s):
  for i in range(len(v)):
    for j in range(len(v)):
      if (v[i] + v[j] == s):
        return [i, j]
  return [0, 0]

print(stsum(v, s))
