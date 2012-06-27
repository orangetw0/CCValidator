# Thiago Militao
# 
# Last revision 6/27
#

# this program is used to verify the Luhn algorithm
# which is used to verify if credit card numbers are valid or not
# by reversing the card number order, doubling up on every other digit, and if the doubled number is bigger than 10 it subtracts 9 as necessary. 
# once that's done it adds up all the sums, if it's divisible by 10, the card number is valid
# otherwise it's an invalid credit card number

import random # import the random stuff

# Uncomment the line below to have it generate a random credit card number and determine if it's valid or not
# card_number = random.randint(16,9999999999999999)

card_number = input("Please enter your full credit card number: (no spaces please) \n> ") # take the user input
cn_string = str(card_number) # turn the card number into a string
cn_list = list(cn_string) # turn each number into a separate item in the list

# verify the 16 digit length
counter = 0 # set the initial counter to 0

for index in range(len(cn_list)): # for every number in the list
	counter = counter + 1 # set the counter to add 1
	
if counter > 16: # if the counter is more than 16, there are too many numbers
	print "Invalid credit card length"
	exit()

if counter < 16: # if the counter is less than 15 there are too little
	print "Invalid credit card length"
	exit()	

cn_reverse = reversed(cn_list) # make the list reversed
cn_rev_string = ''.join(cn_reverse) # join the numbers in the list together
cn_rev_list = list(cn_rev_string) # make the string into a list again
cn_rev = int(cn_rev_string) # make the string into an int
cn_onumber = cn_rev_list [1:16:2] # separate every other number with the exception of the last one
cn_pnumber = cn_list [1::2] # separate every number that wasn't included earlier
doubled = [] # create empty array for the doubled numbers
string_list = [] # create empty array for the final string list 
final_array = [] # create empty array for the final number list

# the following function doubles every other number and if it's greater than 10, subtracts 9 from it
for n in cn_onumber:
	n = int(n) * 2
	if n > 9:
		n = int(n) - 9
	doubled.append(n) # add the doubled numbers to the 'doubled' array

# for each list, add the numbers to the final_list array
for n in cn_pnumber: # for every number that wasn't doubled
	string_list.append(n) # add it to the list
for n in doubled: # for every number that was doubled
	n = str(n) # convert it to a string
	string_list.append(n) # and add it to the list
	
cn_final_string = ''.join(string_list) # make the list into a long string
cn_final = list(cn_final_string) # turn the final converted string back into a list

# convert each number in the final string list into an integer and append to another empty array
for n in cn_final: # for every string in the list
	n = int(n) # convert it to an integer
	final_array.append(n) # and add it to the final array

total = sum(final_array) # sum up all the numbers

# function to determine whether the total is valid or not
def validate(total):
	total = float(total) # convert int to float for decimal
	validation = total / 10 # divide the number by 10
	valid_array = [ 1.0 , 2.0 , 3.0 , 4.0 , 5.0 , 6.0 , 7.0 , 8.0 , 9.0 , 10.0 ] # create array of possible correct answers
	status = "" # set the status to empty string
	for n in valid_array: # for every number in the possible answers
		if validation == n: # if the number in the array matches the total
			status = "Valid" # set status to valid
			print status # show the status
			exit() # and quit all other iterations
		if validation != n: # if the number in the array does not match the total
			status = "Invalid" # set the status to invalid
	print status # print status if all iterations failed
	
# the following 'print' lines are there to show each output from the calculations above
print "Original card number: " , cn_string
print "Number list: " , cn_list
print "Every number that wasn't doubled: " , cn_pnumber
print "Reversed card number order: " , cn_rev
print "Reversed number list: " , cn_rev_list
print "Every other number: " , cn_onumber
print "Array of doubled numbers: " , doubled
print "Array of all the numbers together: " , string_list
print "Big long string: " , cn_final_string
print "Big long final list: " , cn_final
print "Final array with integers: " , final_array
print "Total sum of the calculations: " , total

# run the validate function and determine whether it's valid or not
validate(total)

