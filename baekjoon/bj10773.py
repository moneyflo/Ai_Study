# -*- coding: utf-8 -*-
"""bj10773.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1snXs9hW1nJ5odDXhSfGHdO3KqwDXt5f1
"""

# no.10773
N = int(input())
L = []

for i in range(N):
    num1 = int(input())
    if num1 == 0:
        L.pop()
    else:
        L.append(num1)

sol = sum(L)

print(sol)