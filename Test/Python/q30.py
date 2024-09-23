# Q30. Write a program that prompts the user to enter their age and then prints out whether they
# are a child
# (age 0-12), a teenager (age 13-19), an adult (age 20-59), or a senior (age 60+)

age = int(input('Enter your age: '))
if age < 0:
    print('Invalid age')
elif age <= 12:
    print('child')
elif age <= 19:
    print('teenager')
elif age <= 59:
    print('adult')
else:
    print('senior')