# Q15. Create a function that takes in a tuple of integers and returns the sum of the integers. Test the
# function with a tuple of your choice.

def add(nums:tuple):
    ans = 0
    for num in nums:
        ans += num

    return ans

nums = (1,2,3)
print(add(nums))