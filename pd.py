print('Hello!')
def palindrome():  # function
	string = input('Enter the phrase in lowercase: ')
	if string == string[::-1]: # checking string
		print('This is a palindrome')
	elif string == 'exit' or 'Exit': # exit program
		exit()	
	else:
		print('This isn\'t a palindrome')	
while True: # cycle
	palindrome()