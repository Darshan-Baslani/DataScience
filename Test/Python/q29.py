# Q29. Write a program that generates a random number between 1 and 10 and then prompts the user to
# guess the number. The user has three attempts to guess the number. If the user guesses
# correctly within three attempts, print out "You win!", otherwise print out "You lose!".

import random

target = random.randint(1,10)
tries = 0
print(target)
while tries < 3:
    prediction = int(input('Enter no: '))
    if prediction != target:
        print('Wrong Prediction')
    else:
        print('Congrats, You won!')
        break
    tries += 1
else:
    print('Out of tries.')