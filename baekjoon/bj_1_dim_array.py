# -*- coding: utf-8 -*-
"""bj_1-dim_array.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AFz6KlK2jkzAv3l5yROmws6AOfSnvn12
"""

# 10818
N = int(input())
L = list(map(int, input().split()))
L.sort()

print(L[0], L[len(L)-1])

# 2562
L = []

for _ in range(9):
    n = int(input())
    L.append(n)

m = max(L)
index = L.index(m) + 1

print(m)
print(index)

# 2577

# Dict로 시도했으나 실패
a = int(input())
b = int(input())
c = int(input())

x = a*b*c

cnt = dict()

for i in range(10):
    cnt[i] = 0

print(cnt)

x = str(x)

for i in x:
    i = int(i)
    cnt[i] += 1

for i in range(10):
    print(cnt[i])

print(cnt)

# List로 품
a = int(input())
b = int(input())
c = int(input())

x = a*b*c

x = str(x)
L = []
for i in x:
    L.append(int(i))


for i in range(10):
    print(L.count(i))

# 3052

L = []
cnt = 0

for i in range(10):
    L.append(int(input())% 42)

L = set(L)
L = list(L)

print(len(L))

# 1546
N = int(input())

score = list(map(int, input().split()))

mean = (sum(score) / N) / max(score) * 100

print(mean)

# 8958
N = int(input())

for _ in range(N):
    s = input()
    sol = 0
    n = 0
    for x in s:
        if x == 'O':
            n += 1
            sol += n
        else:
            n = 0
    print(sol)

# 4344
C = int(input())
    
for _ in range(C):
        L =list(map(int, input().split()))
        N = L[0]
        sco = L[1:]
        n = 0
        mean = sum(sco) / N
        
        for x in sco:
            if x > mean:
                n += 1
        
        sol = round(n / N * 100, 3)
        print(f"{sol:.3f}%")