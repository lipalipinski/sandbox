#Guessing Game by JL (lipabass@gmail.com)
#Challenge from the Complete Python 3 Bootcamp by Pierian Data

from random import randint

x = randint(1,100)
delta = 10
guess = None
guess_num = 0 

print('\nWelcome to the Guessing Game!\n')

while guess != x:
	guess = int(input('Guess a number between 1 and 100:\n'))
	
	if guess < 1 or guess > 100:
		print(f'OUT OF BOUNDS!')
		continue	

	guess_num += 1

	delta_new = abs(x - guess)
	if guess_num > 1:
		if delta_new < delta:
			print('WARMER!\n')
		else:
			print('COLDER!\n')	
	else:
		if delta_new < delta:
			print('WARM!\n')
		else:
			print('COLD!\n')
		
	delta = delta_new

print(f'CONGRATULATIONS!\nThe mystery number is {x}, it took you {guess_num} turns to find it!\n')
print('Guessing Game by JL\nfor the Pierian Data Guessing Game Challenge')
