#Guessing Game by JL (lipabass@gmail.com)
#Challenge from the Complete Python 3 Bootcamp by Pierian Data
#v2.1

from random import randint

x = randint(1,100)		#The Mystery Number
delta = [10]			#list of differences between subsequent guesses and the mystery number. [0] is the initial warm/cold threshold
guess = None			#current guessed value
guesses = []			#list of players guesses
plot_line = ''			#chart line

print('\nWelcome to the Guessing Game!\n')

while guess != x:
	guess = input('Guess a number between 1 and 100:\n')

	if guess == '' or guess.isdigit() != True:				#checks if guess is a digit
		continue

	guess = int(guess)

	if guess < 1 or guess > 100:							#checks if guess is within a given range
		print('OUT OF BOUNDS!')
		continue

	guesses.append(guess)

	delta.append(abs(x - guess))
	if len(guesses) > 1: 									#any guess other than 1st
		if guesses[-1] == guesses[-2]:						#exactly same value
			print('Give me something new!\n')
			guesses.pop(-1)
			continue
		else:												#new value
			print('\n')
			if delta[-1] < delta[-2]:
				print('WARMER!\n')
			elif delta[-1] == delta[-2] and delta[-1] <= delta[-3]:
				print('WARM!\n')
			elif delta[-1] == delta[-2] and delta[-1] > delta[-3]:
				print('COLD!\n')
			else:
				print('COLDER!\n')
	else:													#the 1st guess
			if delta[-1] < delta[-2]:
				print('WARM!\n')
			else:
				print('COLD!\n')


print('CONGRATULATIONS!\nThe mystery number is {}, it took you {} turns to find it!\n'.format(x, len(guesses)))

for y in range(len(guesses)):								#chart plot
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
