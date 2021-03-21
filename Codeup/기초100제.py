# 1
print("Hello")

# 2
print("Hello World")

# 3
print("Hello")
print("World")

# 4
print("'Hello'")

# 5
print('"Hello World"')

# 6
print("\"!@#$%^&*()'")

# 7
print("\"C:\\Download\\'hello'.py\"")

# 8
print("print(\"Hello\\nWorld\")")

'''
# 9
c = input()
print(c)


# 10
n = input()
print(n)

# 11
f = input()
print(f)

# 12
a = input()
b = input()
print(a)
print(b)

# 13
a = input()
b = input()
print(b)
print(a)

# 14
a = input()
print(a)
print(a)
print(a)

# 15
a, b = input().split()
print(a)
print(b)

# 16
a, b = input().split()
print(b, a)

# 17
str = input()
print(str, str, str)

# 18
h, m = input().split(':')
print(h,m,sep=':')

# 19
y, m, d = input().split('.')
print(d, m, y, sep='-')

# 20
n1, n2 = input().split('-')
print(n1, n2, sep='')

# 21
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 22
n1 = input()
print(n1[0:2], n1[2:4], n1[4:6])

# 23
h, m, s = input().split(':')
print(m)

# 24
s1, s2 = input().split()
s = s1 + s2
print(s)

# 25
n1, n2 = input().split()    # 리스트에는 int 사용안됨 int() argument must be a string, a bytes-like object or a number, not 'list'
n = int(n1) + int(n2)       # map 사용 까먹지마셈
print(n)

# 26
n1 = input()
n2 = input()
n = float(n1) + float(n2)
print(n)

# 27
n1 = input()
n = int(n1)
print('%x'%n)

# 28
n1 = input()
n = int(n1)
print('%X'%n)

# 29
n1 = input()
n = int(n1, 16)
print('%o'%n)

# 30    <----- Think
n = ord(input())
print(n)

# 31    <----- Think
c = int(input())
print(chr(c))

# 32
n = int(input())
print(-n)

# 33
n1 = input()
n = ord(n1)
print(chr(n+1))

# 34
n1, n2 = input().split()
n = int(n1) - int(n2)
print(n)

# 35
n1, n2 = input().split()
n = float(n1) * float(n2)
print(n)

# 36
w, n = input().split()
print(w*int(n))

# 37
n = input()
s = input()
print(int(n)*s)

# 38
n1, n2 = input().split()
n = int(n1)**int(n2)
print(n)

# 39
n1, n2 = input().split()
n = float(n1)**float(n2)
print(n)

# 40
n1, n2 = map(int, input().split())
print(n1//n2)

# 41
n1, n2 = map(int, input().split())
print(n1%n2)

# 42
n = float(input())
print(round(n, 2))

# 43
f1, f2 = map(float, input().split())
f = f1 / f2
print('%.3f'%f)

# 44
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(round(a/b, 2))

# 45
a, b, c = map(int, input().split())
s = a+b+c
avg = s / 3
print(s, round(avg, 2))

# 46
n = int(input())
print(n<<1)

# 47
n1, n2 = map(int, input().split())
print(n1<<n2)

# 48
n1, n2 = map(int, input().split())
print(n1<n2)

# 49
n1, n2 = map(int, input().split())
print(n1==n2)

# 50
n1, n2 = map(int, input().split())
print(n1<=n2)

# 51
n1, n2 = map(int, input().split())
print(n1!=n2)

# 52 <--- 정수값 0 만 False로 표현됨
n = int(input())
print(bool(n))

# 53
a = bool(int(input()))
print(not a)

# 54
a, b = map(int, input().split())
print(bool(a) and bool(b))

# 55
a, b = map(int, input().split())
print(bool(a) or bool(b))

# 56
a, b = map(int, input().split())
print(bool(a != b))

# 57
a, b = map(int, input().split())
print(bool(a == b))

# 58
a, b = map(int, input().split())
c = bool(a)
d = bool(b)
print(not(a or b))

# 59    ## ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
#          <<(bitwise left shift), >>(bitwise right shift)
a = int(input())
b = ~a
print(b)

# 60
a, b = map(int, input().split())
print(a & b)

# 61
a, b = map(int, input().split())
print(a | b)

# 62
a, b = map(int, input().split())
print(a ^ b)

# 63
a, b = map(int, input().split())
c = (a if (a>=b) else b)
print(int(c))

# 64
a, b, c = map(int, input().split())
d = (a if a < b else b)
e = (d if d < c else c)
print(int(e))

# 65
a, b, c = map(int, input().split())

if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

# 66
a, b, c = map(int, input().split())
d = [a, b, c]

for i in d:
    if i % 2 ==0:
        print("even")
    else:
        print("odd")

# 67
a = int(input())

if (a < 0) and (a % 2 == 0):
    print("A")
elif (a < 0) and (a % 2 != 0):
    print("B")
elif (a > 0) and (a % 2 == 0):
    print("C")
elif (a > 0) and (a % 2 != 0):
    print("D")
else:
    print("0 입니다.")

# 68
n = int(input())

if n >= 90:
    print("A")
elif n >= 70:
    print("B")
elif n >= 40:
    print("C")
else:
    print("D")

#69
a = input()

if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")

# 70
ss = int(input())

if ss//3 == 1:
    print("spring")
elif ss//3 == 2:
    print("summer")
elif ss//3 == 3:
    print("fall")
else:
    print("winter")

# 71
n = 1
while n!=0:
    n = int(input())
    if n!=0:
        print(n)

# 72
n = int(input())
while n!=0:
    print(n)
    n = n-1

# 73
n = int(input())
while n!=0:
    n = n - 1
    print(n)

# 74
c = ord(input())
t = ord('a')
while t<=c:
    print(chr(t), end=' ')
    t += 1
'''
# 75
n = int(input())
t = 0
while t<=n:
    print(t)
    t += 1
