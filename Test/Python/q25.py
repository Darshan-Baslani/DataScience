# Q25. Write a program that prompts the user to enter a number between 1 and 10. If the number is less than
# 5, print out "Too low!", otherwise print out "Too high!".

num = int(input('Enter a number: '))
if num < 5:
    print('Too Low')
else:
    print('Too high')