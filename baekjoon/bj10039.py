L = []

for i in range(5):
    n = int(input())
    if n < 40:
        n = 40
    L.append(n)

print(int(sum(L) / 5))
