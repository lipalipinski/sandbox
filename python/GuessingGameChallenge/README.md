# Guessing Game Challenge

Writing this script was part of the 2022 Complete Python Bootcamp by Pierian Data.
Here are the conditions it should meet:

>Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
>
>* If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
>* On a player's first turn, if their guess is
>  * within 10 of the number, return "WARM!"
>  * further than 10 away from the number, return "COLD!"
>* On all subsequent turns, if a guess is
>  * closer to the number than the previous guess return "WARMER!"
>  * farther from the number than the previous guess, return "COLDER!"
>* When the player's guess equals the number, tell them they've guessed correctly and >how many guesses it took!

In **Guessing Game 2** I have made some improvements:
* v2.0:
  * a plot showing player's path to guessing the mystery number.
* v2.1:
  * ignores the guess if guess value is the same as the previous one, and prompt "Give me something new" message.
  * asks for a value again if player puts non integer value as a guess or presses ENTER key without entering a number.
  * returns "WARM!" or "COLD!" if the distance between new guess and the previous one is the same. "WARM!" if the distance is smaller than two guesses before (or than the initial cold/warm threshold), "COLD!" otherwise.

*JL 2022*
