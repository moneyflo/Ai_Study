# -*- coding: utf-8 -*-
"""bj1026.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vvQYJZgIjrowwKpY9UexhNrB6JiN3tQj
"""

# no.1026
N = int(input())
a = map(int, input().split())
b = map(int, input().split())

a = sorted(a)
b = sorted(b, reverse=True)

L = [a[i] * b[i] for i in range(N)]
sol = sum(L)
print(sol)

a = [1,2,3]
b = permutations(a)
b1 = list(b)
print(b1[0])

type(a)
print(b)