# -*- coding: utf-8 -*-
"""bj2164.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mySpH68sLDZdcGtgpCNTmPMTmYb5523B
"""

# no.2164
N = int(input())

L = list(range(N))
cnt = len(L)
L = [L[i] for i in range(1, len(L), 2)]

while len(L) > 1:
    if cnt % 2 != 0:
        cnt += len(L)
        L = [L[i] for i in range(0, len(L), 2)]
    else:
        cnt += len(L)
        L = [L[i] for i in range(1, len(L), 2)]


if L:
    print(L[0]+1)
else:
    print(1)

a = [1, 2, 3, 4, 5]
a = [a[i] for i in range(0, len(a), 2)]
print(a)