# -*- coding: utf-8 -*-
"""bj1764.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EYc-iXGOjqoeewwPXxYrD2Xrhz7vODu-
"""

# no.1764
N, M = map(int, input().split())

d = []
b = []

for _ in range(N):
    tmp = input()
    d.append(tmp)

for _ in range(M):
    tmp = input()
    b.append(tmp)

d = set(d)
b = set(b)

sol = d & b
sol = list(sol)

sol = sorted(sol)

print(len(sol))

for x in sol:
    print(x)

