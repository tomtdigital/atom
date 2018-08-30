#Currently running on Python Version 3.7 (32-bit)

#Imports used for random numbers and time delays
import random
import time

#Upon welcome
print ('Welcome to Bingo Caller Version 3.7')
print ('After you type a value, press ENTER to submit it.')
#Pauses to emphasise the above statement
time.sleep(5)

#Declares function for main process
def begin():
	#Without try and except, the program would fail if the values entered by the user weren't integers.
	try: no_of_rounds = int(input('How many numbers would you like generated for this game? '))
	except ValueError:
		print ('Please enter a valid number')
		begin()
	#Checks if the user is happy with the amount of numbers being called in the game
	confirm_rounds = input('Are you sure? Enter \'y\' for yes and \'n\' for no: ')
	#If happy...
	if confirm_rounds == 'y':
		print ('Lets play Bingo!')
		ready = input('Press ENTER to get your first number: ')
		#To start the game, the user can hit ENTER. Any other value is also accepted to avoid errors.
		if ready >= '':
			#The game has started, and a variable is declared as a random number between 0 and 90
			next_num = random.randint(1,91)
			#A list is created for numbers already called to go in
			already_called = []
			#A while loop is initiated, so long as x is less than the number of rounds inputted on line 16
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
			
			#A function is declared, checking if the user would like to play again. If they do, it runs the main process again.
			def play_again():
				again = input('Would you like to play again? Enter \'y\' for yes and \'x\' to exit: ')
				if again == 'y':
					begin()
				elif again == 'x':
					print ('Goodbye!')
					time.sleep(2)
					exit()
				#In case they enter a different value
				else: 
					play_again()
			
			#Runs the function at the end of the game.
			play_again()
	
	#If the user changes their mind about the amount of numbers being called out. 		
	else :
		begin()

#Actually runs the game
begin()