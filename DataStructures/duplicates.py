m = [2,5,5,5]
n = [2,2,3,5,5,7]
s = []
for i in range(len(m)):
	for j in range(len(n)):	
		#print(str(m[i]) + " " + str(n[j])) Line for debugging
		if n[j] == m[i] and n[j] != -1: 
			s.append(n[j])
			n[j] = -1
			m[i] = -1


for val in s:
	print(str(val) + " "),
