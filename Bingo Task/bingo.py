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
			next_num = random.randint(1,90)
			#A list is declared, that will store each number called
			already_called = []
			#A function is declared. It prints a random number, and pauses for a set time to allow the bingo caller to announce it.
			def play_bingo():
				#Resets if the number has already been called
				if next_num in already_called:
					play_bingo()
				#Otherwise, the number is stored with business as usual
				else:
					print (next_num)
					already_called.append(next_num)
					print ('Confirming next number...')
					time.sleep(5)
			#This function then runs for the amount of times that was earlier inputted on line 16	
			for x in range (no_of_rounds):
				play_bingo()
				#Re-declaring the variable resets the number after it has been called.
				next_num = random.randint(1,90)
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
	elif confirm_rounds == 'n':
		begin()
	else :
		begin()

#Actually runs the game
begin()