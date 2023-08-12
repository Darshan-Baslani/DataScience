# Q5. Can you write a program that determines the nature of a given number (in this case, 87) as being
# positive, negative, or zero? The program should be designed to take the number as input and perform the
# necessary calculations to determine if the number is positive (i.e., greater than zero), negative
# (i.e., less than zero), or zero (i.e., equal to zero). The output of the program should indicate which of these
# three categories the given number falls into
num = int(input('Enter any no: '))
if num < 0:
    print('Negative')
elif num > 0:
    print('Positive')
else:
    print('Zero')
