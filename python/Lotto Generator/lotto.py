# sktypt generuje wyniki zadanej liczby losowań Lotto i zapisuje je w pliku "wyniki lotto.txt".
# JL 2022

from random import randint
from time import localtime, strftime

losowanie = []
wyniki = []

liczba_losowan = int(input('\nWitaj w LOTTO GENERATOR by JL\n\nIle losowań chcesz przeprowadzić?\n')) 
print('\nBęben maszyny losującej jest pusty, następuje zwolnienie blokady...')

for numer_losowania in range(liczba_losowan):
    while len(losowanie) < 6:
        wylosowana = randint(1,49)
        if wylosowana in losowanie:
            continue
        else:
            losowanie.append(wylosowana)
    losowanie = sorted(losowanie)
    wyniki.append(losowanie)
    losowanie = []

godz_los = strftime('%H:%M', localtime())
data_los = strftime('%d.%m.%Y', localtime())

print(f'\nWYNIKI {liczba_losowan} LOSOWAN PRZEPROWADZONYCH O GODZINIE {godz_los}:\n')
for numer, wynik in enumerate(wyniki):
	print(f'Losowanie nr {numer + 1}: \n {wynik}\n') 

with open('wyniki lotto.txt', mode ='w') as file:
    file.write(f'Wyniki {liczba_losowan} losowań przeprowadzonych {data_los} o godzinie {godz_los}:\n\n')

with open('wyniki lotto.txt', mode='a') as file:
    for numer, wynik in enumerate(wyniki):
        file.write(f'Losowanie nr {numer + 1}: \n {wynik}\n\n')

print(f'\nWyniki {liczba_losowan} losowań zapisano w pliku "wyniki lotto.txt"')
print('LOTTO GENERATOR by JL 2022')
