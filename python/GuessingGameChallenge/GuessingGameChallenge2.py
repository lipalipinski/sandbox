#Guessing Game by JL (lipabass@gmail.com)
#Challenge from the Complete Python 3 Bootcamp by Pierian Data

from random import randint

x = randint(1,100)
delta = 10
guess = None
guesses = []
plot_line = ''

print('\nWelcome to the Guessing Game!\n')

while guess != x:
	guess = int(input('Guess a number between 1 and 100:\n'))
	
	if guess < 1 or guess > 100:
		print(f'OUT OF BOUNDS!')
		continue	

	guesses.append(guess)	

	delta_new = abs(x - guess)
	if len(guesses) > 1:
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

print('CONGRATULATIONS!\nThe mystery number is {}, it took you {} turns to find it!\n'.format(x, len(guesses)))

for y in range(len(guesses)):
	plot_line += '{0:4}'.format(str(y+1)+'.') + '|'
	for j in range(100):
		if j+1 == x == guesses[y]:
			plot_line += 'X'	
		elif j+1 == x:
			plot_line += '.'
		elif j+1 == guesses[y]:
			plot_line += 'o'
		else:
			plot_line += ' '
	plot_line += '|'
	print(plot_line)
	plot_line = ''


print('\nGuessing Game by JL for the Pierian Data Guessing Game Challenge\n2022')

