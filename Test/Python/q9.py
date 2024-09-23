# Q9.Write a program to check if a given number 371 is an Armstrong number?

digits = 0
num = int(input('Enter a no:'))
temp_num = num
while temp_num > 0:
    digits += 1
    temp_num = int(temp_num / 10)

ans = 0
temp_num = num
while temp_num > 0:
    ans += (temp_num % 10) ** digits
    temp_num = int(temp_num / 10)

if ans == num:
    print(f'{num} is palindrome')
else:
    print(f'{num} is not palindrome')