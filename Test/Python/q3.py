# Q3.Write a program that prints all prime numbers between 0 and 50.
for i in range(0, 51):
    condition = True
    j = 2
    while j < i:
        if i % j == 0:
            condition = False
            break
        j += 1
    if condition:
        print(i)
