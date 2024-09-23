# Q8.Write a program for reversing the given number 5436 and the output should be 6345.

rev = 0
num = 5436
while num > 0:
    rev = (rev * 10) + num % 10
    num = int(num / 10)

print(rev)