#Guessing Game by JL (lipabass@gmail.com)
#Challenge from the Complete Python 3 Bootcamp by Pierian Data
#v2.2

from random import randint

x = randint(1,70)		#The Mystery Number
delta = [10]			#list of differences between subsequent guesses and the mystery number. [0] is the initial warm/cold threshold
guesses = []			#list of players guesses

def player_guess():
	"""
	Asks player for an int within 1-70 range
	Prints "OUT OF BOUNDS!" if given value is not within a range
	Returns int
	"""
	new_guess = None
	while new_guess not in list(range(1,70)):
			new_guess = input('Guess a number between 1 and 70:\n')
			if new_guess.isdigit() != True:
				continue
			else:
				new_guess = int(new_guess)
				if new_guess not in list(range(1,70)):		#checks if guess is within a given range
					print('OUT OF BOUNDS!')
	return new_guess

def chart_plot(g_list, x, w, disp = ''):
	"""
	Plots a chart of guesses from g_list, indicating a mystery number x, plot area width w
	Marks x on every line if disp = 'y'
	Max number of guesses is 99
	"""
	plot_line = ''			#chart line

	print(' ' * 5 + '_' * w )

	for y, g in enumerate(g_list):
		plot_line += '{0:4}'.format(str(y+1)+'.') + '|'
		for j in range(w):
			if j+1 == x == g:
				plot_line += 'X'
			elif j+1 == x and disp == 'y':
				plot_line += '.'
			elif j+1 == g:
				plot_line += 'o'
			else:
				plot_line += ' '
		plot_line += '|'
		print(plot_line)
		plot_line = ''

	print(' ' * 5 + '-' * w )

#================ CLR SCREEN =================
def clr_scr():
	print('\n'*100)



#=========== START ==================

clr_scr()
print('\nWelcome to the Guessing Game!\n')

while len(guesses) == 0 or guesses[-1] != x:


	guesses.append(player_guess())							#getting a guess
	delta.append(abs(x - guesses[-1]))
	print('')

	if guesses[-1] != x:
		chart_plot(guesses, x, 70)								#progress chart

		if len(guesses) == 1: 									#the first guess
			if delta[-1] < delta[-2]:
				print(f'{guesses[-1]} is WARM!\n')
			else:
				print(f'{guesses[-1]} is COLD!\n')
		else:													#subsequent guesses
			if guesses[-1] == guesses[-2]:						#exactly same value
				print('Give me something new!\n')
				guesses.pop(-1)
				continue
			else:												#new value
				if delta[-1] < delta[-2]:
					print(f'{guesses[-1]} is WARMER!\n')
				elif delta[-1] == delta[-2] and delta[-1] <= delta[-3]:
					print(f'{guesses[-1]} is WARM!\n')
				elif delta[-1] == delta[-2] and delta[-1] > delta[-3]:
					print(f'{guesses[-1]} is COLD!\n')
				else:
					print(f'{guesses[-1]} is COLDER!\n')											#the 1st guess


print('CONGRATULATIONS!')
chart_plot(guesses, x, 70, 'y')
print('The mystery number is {}, it took you {} turns to find it!\n'.format(x, len(guesses)))

print('\nGuessing Game by JL\n2022')
