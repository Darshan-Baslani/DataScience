# Q11. Create a list in python using the followings: 2,3,4,5,6,7 with variable ‘a’
# Add ‘mango to the above list
# Also add banana, grapes & orange in the list
# insert apple in the 5th position of a variable ‘a’
# Remove last item from the list
a = [2,3,4,5,6,7]
print(a)
a.append('mango')
print(a)
a.extend(['banana', 'grapes' , 'orange'])
print(a)
a.insert(5, 'apple')
print(a)
del a[-1]
print(a)