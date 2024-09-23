# Q27. Write a program that prompts the user to enter a positive integer. Then, use a loop to print out all the
# odd numbers from 1 to that integer

target = int(input("Enter target: "))
for i in range (1, target+1):
    if i % 2 != 0:
        print(i)