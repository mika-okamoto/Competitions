import math
n, k = map(int, input().split())
print(math.ceil(n*8/k) + math.ceil(n*5/k) + math.ceil(n*2/k))
