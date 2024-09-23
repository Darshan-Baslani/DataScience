# Q20. Write a Python program to find the difference between consecutive numbers in a list
nums = [1,3,5,6,10]
answers = []
for i in range(len(nums)-1):
    answer = nums[i+1] - nums[i]
    answers.append(answer)

print(answers)