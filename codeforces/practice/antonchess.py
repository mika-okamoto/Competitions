n = int(input())
g = input()
a, d = 0, 0
for c in g:
    if c == "A":
        a += 1
    else:
        d += 1
if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")