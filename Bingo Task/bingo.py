#Currently running on Python Version 3.7 (32-bit)

#Imports used for random numbers and time delays
import random
import time

#Upon welcome
print ('Welcome to Bingo Caller Version 3.7')
print ('After you type a value, press ENTER to submit it.')
#Pauses to emphasise the above statement
time.sleep(5)

#Main process
def begin():
	try: no_of_rounds = int(input('How many numbers would you like generated for this game? '))
	except ValueError:
		no_of_rounds = int(input('Please enter a valid number '))
	#Checks if the user is happy with the amount of numbers being called in the game
	confirm_rounds = input('Are you sure? Enter \'y\' for yes and \'n\' for no: ')
	#Loops until valid input
	while confirm_rounds != 'y' and confirm_rounds != 'n':
		confirm_rounds = input('Invalid input. Enter \'y\' for yes and \'n\' for no: ')
	
	#Loops until user sure about the number of rounds
	while confirm_rounds == 'n':
		try: no_of_rounds = int(input('How many numbers would you like generated for this game? '))
		except ValueError:
			no_of_rounds = int(input('Please enter a valid number '))
		confirm_rounds = input('Are you sure? Enter \'y\' for yes and \'n\' for no: ')
		while confirm_rounds != 'y' and confirm_rounds != 'n':
			confirm_rounds = input('Invalid input. Enter \'y\' for yes and \'n\' for no: ')
	
	#If happy, the above loops end, and the code continues
	if confirm_rounds == 'y':
		print ('Lets play Bingo!')
		ready = input('Press ENTER to get your first number: ')
		#To start the game, the user can hit ENTER. Any other value is also accepted to avoid errors.
		if ready >= '':
			#The game has started, and a variable is declared as a random number between 0 and 90
			next_num = random.randint(1,91)
			#A list is created for numbers already called to go in
			already_called = []
			#A while loop is initiated, so long as x is less than the number of rounds inputted on line 17
			x = 0
			while x < no_of_rounds:
				#The number is reset if it has already been called; x stays the same
				if next_num in already_called:
					next_num = random.randint(1,91)
				#If the number hasn't been called, then it is included in the list, printed, and reset. x then increases by 1						
				elif next_num not in already_called:
					already_called.append(next_num)
					print (next_num)
					next_num = random.randint(1,91)
					time.sleep(5)	
					x +=1
				#Ends the loop when conditions met				
				else:
					break
				
			#When all numbers are called...
			print ('Total numbers reached.')
			time.sleep(2)
			print ('Thank you for playing!')
			

	
			
#Actually runs the game
begin()
#Asks if they want to play again
again = input('Would you like to play again? Enter \'y\' for yes and \'x\' to exit: ')
#Loops until valid input
while again != 'y' and again != 'x':
	again = input('Invalid input. Enter \'y\' for yes and \'x\' to exit: ')
#The game loops until the user declares 'x'
while again == 'y':
	begin()
	again = input('Would you like to play again? Enter \'y\' for yes and \'x\' to exit: ')
if again == 'x':
	print ('Goodbye!')
