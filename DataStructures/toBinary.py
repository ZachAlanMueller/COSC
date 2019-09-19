import math

n = 21
pre = []
b = []
while n != 0:
	pre.append(int(n % 2))
	n = math.floor(n/2)
for i in range(len(pre)):
	b.append(pre[len(pre)-i -1])

for val in b:
	print(str(val))