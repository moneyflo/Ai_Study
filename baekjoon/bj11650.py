# -*- coding: utf-8 -*-
"""bj11650.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FVu56ROxkRNGyPTNzwHIHYpuMtXSBzDq
"""

# 11650
N = int(input())
L = []

for _ in range(N):
    a, b = map(int, input().split())
    L.append((a,b))

sol = sorted(L, key = lambda x : (x[0], x[1]))

for x in sol:
    print(x[0], x[1])


# 시간초과뜸
# sys.stdin.readline 쓰니까 풀림

