import random

def match(val, gloves_picked):
	#Debugging lines
	# print("Search Value: " + str(val) + " | "),
	# for x in gloves_picked:
	# 	print(x),
	# print("")
	#Debugging lines end
	compliment = val
	if(val % 2 == 0):
		compliment -= 1
	else:
		compliment += 1
	#print(compliment)
	for x in gloves_picked:
		if(x == compliment):
			#print("Match Found")
			return True
	return False

def drawer():
	num_in_drawer = 22
	gloves_drawer = [11,11,11,11,11,12,12,12,12,12,21,21,21,21,22,22,22,22,31,31,32,32]
	gloves_picked = []
	picked_so_far = 0
	while(num_in_drawer != 0):
		choice = random.randint(0,21)
		if(gloves_drawer[choice] != 0):
			if(match(gloves_drawer[choice], gloves_picked) == True):
				print("--- MATCH ---")
				print("Gloves Picked | "),
				for x in gloves_picked:
					print(x),
				print("\nLast Glove Picked | " + str(gloves_drawer[choice]))
				print("Iterations | " + str(len(gloves_picked)+1) + "\n")
				return(len(gloves_picked)+1)

			gloves_picked.append(gloves_drawer[choice])
			match(gloves_drawer[choice], gloves_picked)
			picked_so_far = picked_so_far + 1
			gloves_drawer[choice] = 0
			num_in_drawer = num_in_drawer -1

	print("Gloves Drawer:"),
	for x in range(len(gloves_drawer)): 
	    print (gloves_drawer[x]),
	    print(""), #this line is just for formatting in terminal output

	print("\nGloves Picked:"),
	for x in range(len(gloves_picked)): 
	    print (gloves_picked[x]),

def main():
	total = 0.0
	n = 10000
	for x in range(n):
		total = total + drawer()
	#print(total)
	print("Average for n=" + str(n) + ": "),
	print(str(total/n))

main()