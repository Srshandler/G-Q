# 3-sum 1
#v - vetor
#s - soma
# retorna um vetor com i,j
v = [1, 3, 5, 7, 11, 2, 4, 8, 12]
s = -65353


def stum(v, s):
  for i in range(len(v)):
    for j in range(i + 1, len(v)):
      if (v[i] + v[j] == s):
        return [i, j]
  return [0, 0]


print(stum(v, s))
