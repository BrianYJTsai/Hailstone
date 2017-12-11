#  File: Hailstone.py

#  Description: This program generates the hailstone sequence for a range of user defined numbers
#  The user inputs the start and end range of the numbers they want to verify and the output is the number 
#  within the range that has the longest hailstone sequence.  

#  Student Name: Brian Tsai

#  Student UT EID: byt76

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 2/17/17

#  Date Last Modified: 2/17/17
import random

# Function that uses recursion to count the number of cycles for an input number
def change_number(number):
	if (number == 1): # If the number is equal to 1, then end the recursion
		return 0
	elif (number % 2 == 0):
		return 1 + change_number(number // 2) # If the number is even, then divide it by 2 and add 1 to the number of cycles
	else:
		return 1 + change_number(3 * number + 1) # If the number is odd, then multiply by 3 and add 1, also add 1 to the number of cycles

def main():
	# correct_input is True when the user inputs valid numbers
	correct_input = False 

	# Prompt the user until the inputs are valid
	while (not correct_input):
		start_number = eval(input("Enter starting number of the range: ")) # Start number input 
		end_number = eval(input("Enter ending number of the range: ")) # End number input 
		if (start_number > 0 and end_number > 0 and (end_number - start_number > 0)): # Both inputs must be positive and end must be larger than start
			correct_input = True

	# number_list holds a list of the numbers to be tested		
	number_list = list(range(start_number, end_number + 1))	
	# cycle_list holds a list of the number of cycles for each number
	cycle_list = []	

	# Iterate through each number and put its cycles into cycle_list after being called
	for number in range(start_number, end_number + 1):
		cycle_list.append(change_number(number))

	# max_list holds a list of the indexes of the number with the greatest cycle
	max_list = []

	# max_cycle holds the largest cycle number
	max_cycle = max(cycle_list)	

	# Iterate through cycle_list and store the indexes of the numbers in max_list
	for max_index, max_value in enumerate(cycle_list): 
		if (max_value == max_cycle): 				
			max_list.append(max_index) # If the number in cycle_list matches the largest cycle number, then add the index to max_list

	# max_index holds the largest cycle indexes, multiple numbers can be in max_list and max_index will choose the largest number 
	max_index = max_list[-1]

	# Print the number associated with the index in max_index as well as the cycle number				
	print("The number", number_list[max_index], "has the longest cycle length of", cycle_list[max_index], end=". \n") 

main()
