# Q10.Write a program the given year is 1996, a leap year.
# I think the question is - to find whether a given year is leap year or not
year = int(input('Enter a year: '))
if year % 4 == 0:
    print('Leap Year')
else:
    print('Not Leap Year')