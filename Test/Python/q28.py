# Q28. Write a program that generates a random number between 1 and 100 and then prompts the user to
# guess the number. If the user's guess is too low, print out "Too low!", if the guess is too high,
# print out "Too high!", and if the guess is correct, print out "You win!".

import random

target = random.randint(1,100)
while True:
    prediction = int(input('Enter no: '))
    if prediction < target:
        print('Too low')
    elif prediction > target:
        print('Too high')
    else:
        print('Congrats, You won!')
        break