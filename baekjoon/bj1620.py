n, m = map(int, input().split())

d1 = {}
d2 = []


for i in range(1,n+1):
    d1['{}'.format(i)] = input()

re_d1 = dict(map(reversed, d1.items()))
for i in range(m):
    d2.append(input())


for x in d2:
    if d1.get(x) == None:
        print(re_d1.get(x))
    else:
        print(d1.get(x))


