import random
def verify(st1, st2, st3, unique, trial):
	#unique[x] = trial[x]
	#create num1, num2, num3 and verify they add together, return boolean
	num1 = 0
	for i in range(0, len(st1)):
		for j in range(0,len(unique)):
			if(st1[i] == unique[j]):
				num1 += (trial[j])*(10**(len(st1)-i-1))
	num2 = 0
	for i in range(0, len(st2)):
		for j in range(0,len(unique)):
			if(st2[i] == unique[j]):
				num2 += (trial[j])*(10**(len(st2)-i-1))
	num3 = 0
	for i in range(0, len(st3)):
		for j in range(0,len(unique)):
			if(st3[i] == unique[j]):
				num3 += (trial[j])*(10**(len(st3)-i-1))

	print(num1)
	print(num2)
	print(num3)
	if((num1+num2) == num3):
		return True
	return False

def main():
	st1 = "SEND"
	st2 = "MORE"
	st3 = "MONEY"
	unique_letters = ""
	starters = []
	#St1 Loop
	for i in st1:
		isValid = 1
		for j in unique_letters:
			if(j == i):
				isValid = 0
		if(isValid == 1):
			unique_letters+=str(i)
			if(i == st1[0]):
				starters.append(len(unique_letters)-1)
	#St2 Loop
	for i in st2:
		isValid = 1
		for j in unique_letters:
			if(j == i):
				isValid = 0
		if(isValid == 1):
			unique_letters+=str(i)
			if(i == st2[0]):
				starters.append(len(unique_letters)-1)
	#St3 Loop
	for i in st3:
		isValid = 1
		for j in unique_letters:
			if(j == i):
				isValid = 0
		if(isValid == 1):
			unique_letters+=str(i)
			if(i == st3[0]):
				starters.append(len(unique_letters)-1)
	print(unique_letters)
	if(len(unique_letters) > 9):
		print("Too many unique letters")
	trial_digits = []

	for i in range(0,len(unique_letters)):
		tmp = random.randint(0,9)
		complete = 0
		while complete == 0:
			tmp = random.randint(0,9)
			isValid = 1
			complete = 0
			zeroCheck = 1
			for k in range(0, len(starters)):
				if((starters[k] == i) and tmp == 0):
					zeroCheck = 0
			for j in range(0,len(trial_digits)):
				if(tmp == trial_digits[j]):
					isValid = 0

			if(isValid == 1 and zeroCheck == 1):
				trial_digits.append(tmp)
				complete = 1
	#print("."),
	print(trial_digits)

	if(verify(st1, st2, st3, unique_letters, trial_digits)):

		print("\nSolution: ")
		print("ST1: " + st1 + "\tST2: " +st2 + "\tST3: " + st3)
		print("Unique Letters: \t" + unique_letters)
		print("Trial Digits: \t"),
		print(trial_digits)
		exit()
	exit()



while(True):
	main()





















