# Q7.Write a program for sum of digits.The digits are 76543 and the output should be 25.

ans = 0
num = 76543
while num > 0:
    ans += num%10
    num =int(num / 10)

print(ans)