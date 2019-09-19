def format(num, length):
	returnValue = ""
	if num[0] == "1":
		for i in range(0,length - len(num)):
			returnValue+="1"
	if num[0] == "0":
		for i in range(0,length - len(num)):
			returnValue+="0"
	returnValue += num
	return returnValue

def twosCompliment(num):
	result = ""
	for i in range(0,len(num)):
		j = (len(num) - i - 1) #start from end of string and work backwards
		if(num[i] == "1"):
			result+="0"
		else:
			result+="1"
	result = addBinary(result,"0001")
	return result


def addBinary(num1, num2):
	result = ""
	if (len(num1) != len(num2)):
		if(len(num1) > len(num2)):
			num2 = format(num2, len(num1))
		else:
			num1 = format(num1, len(num2))

	#confreaking grats they are the same length now
	carryOver = "0"
	for i in range(0,len(num1)):
		j = (len(num1) - i - 1) #start from end of string and work backwards
		if(num1[j] == "1" and num2[j] == "1" and carryOver == "1"):
			tmp = result
			result = "1"
			result+=tmp #python sucks w/ strings
			carryOver = "1"
		elif (num1[j] == "1" and num2[j] == "1" and carryOver == "0"):
			tmp = result
			result = "0"
			result+=tmp #python sucks w/ strings
			carryOver = "1"
		elif (num1[j] == "1" and num2[j] == "0" and carryOver == "1"):
			tmp = result
			result = "0"
			result+=tmp #python sucks w/ strings
			carryOver = "1"
		elif (num1[j] == "1" and num2[j] == "0" and carryOver == "0"):
			tmp = result
			result = "1"
			result+=tmp #python sucks w/ strings
			carryOver = "0"
		elif (num1[j] == "0" and num2[j] == "1" and carryOver == "1"):
			tmp = result
			result = "0"
			result+=tmp #python sucks w/ strings
			carryOver = "1"
		elif (num1[j] == "0" and num2[j] == "1" and carryOver == "0"):
			tmp = result
			result = "1"
			result+=tmp #python sucks w/ strings
			carryOver = "0"
		elif (num1[j] == "0" and num2[j] == "0" and carryOver == "1"):
			tmp = result
			result = "1"
			result+=tmp #python sucks w/ strings
			carryOver = "0"
		elif (num1[j] == "0" and num2[j] == "0" and carryOver == "0"):
			tmp = result
			result = "0"
			result+=tmp #python sucks w/ strings
			carryOver = "0"
	return result





def multiplyBinary(multiplicand, multiplier):
	lastBit = "0"
	runningResult = ""
	for i in range(0,len(multiplier)):
		runningResult += "0"
	runningResult+=str(runningResult)
	currentShift = 0

	for i in range(0,len(multiplier)):
		j = (len(multiplier) - i - 1) #start from end of string and work backwards
		if (multiplier[j] == lastBit):
			#do nothing
			j=j #this does absolutley nothing but I need it
		elif (multiplier[j] == "1"):
			#subtract multiplicand
			# print("Subtracting Multiplicand\t"),
			tmp = twosCompliment(multiplicand)
			for i in range(0,currentShift):
				tmp+=str("0")
			# print(tmp)
			runningResult = addBinary(runningResult, tmp)
			#do subtract
		else:
			#add multiplicand
			# print("Adding Multiplicand\t"),
			tmp = multiplicand
			for i in range(0,currentShift):
				tmp+=str("0")
			# print(tmp)
			runningResult = addBinary(runningResult, tmp)
			#do add
		currentShift += 1
		lastBit = multiplier[j]
	return runningResult





def main():
	num1 = raw_input("Please enter first byte: ")
	num2 = raw_input("Please enter second byte: ")
	result = multiplyBinary(str(num1), str(num2))

	print("    "+num1)
	print("x   "+num2)
	print(result + "\n")
	#Manual tests I did
	# num1 = "0011" #3
	# num2 = "0110" #6
	# result = multiplyBinary(num1, num2)
	# print("    "+num1 + " (3)")
	# print("x   "+num2 + " (6)")
	# print(result + " (18)" + "\n")

	# num1 = "0101" #5
	# num2 = "0001" #1
	# result = multiplyBinary(num1, num2)
	# print("    "+num1 + " (5)")
	# print("x   "+num2 + " (1)")
	# print(result + " (5)" + "\n")

	# num1 = "0111" #7
	# num2 = "1001" #-7
	# result = multiplyBinary(num1, num2)
	# print("    "+num1 + " (7)")
	# print("x   "+num2 + " (-7)")
	# print(result + " (-49)" + "\n")



main()