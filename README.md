# Sandbox
## by JL (lipabass@gmail.com)

This repository contains simple, training projects I have created during courses and bootcamps.

## Content
### Python 3.9.7
 * Lotto Generator

   My very first project in python. Generates desired number of 6 unique, random number sets, and saves them in "wyniki lotto.txt".

 * Guessing Game

   First assignment from the Perian Data 2022 Complete Python Bootcamp. Player has to guess the number between 1 and 100.
   The game tells, whether each guess is closer to the target than the previous one. It also tells whether the first guess
   is closer, or further than 10 from the target.

 * Guessing Game 2

   Added some improvements to the original Guessing Game:
   * v2.0:
     * a plot showing player's path to guessing the mystery number.
   * v2.1:
     * ignores the guess if guess value is the same as the previous one, and prompt "Give me something new" message.
     * asks for a value again if player puts non integer value as a guess or presses ENTER key without entering a number.
     * returns "WARM!" or "COLD!" if the distance between new guess and the previous one is the same. "WARM!" if the distance is smaller than two guesses before (or than the initial cold/warm threshold), "COLD!" otherwise.

*JL 2022*
