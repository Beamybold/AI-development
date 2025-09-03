#List operation
#concatenation: joining 2 lists into a new list
list1 = [1, 2, 3, 4, 8]
list2 = [4, 5, 6,]
results = list1 + list2
print(results)

#repetition (*)
nums = [1, 2]
repeated = nums * 4
print(repeated)

#indexing: access elements using their position
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[-1])  # cherry (negative index starts from the end)

# slicing to extract a portion of the list
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])   # starts from 1 and ends on 4
print(numbers[:3])    # first 3 from the front
print(numbers[3:])    # last 3
print(numbers[::2])   # step of 2, ie first one in the space of 2

# Checks if an element exists in a list.
colors = ["red", "green", "blue"]
print("green" in colors)   
print("yellow" not in colors)  

#lenghth (len()) to count the no of elements in a list
items = ["pen", "book", "laptop"]
print(len(items))  # 3

#min() and max()
nums = [5, 2, 9, 1]
print(min(nums))  
print(max(nums))  

#(sum())
numbers = [1, 2, 3, 4]
print(sum(numbers))  

#list comprehensiom to create a list in asingle line
squares = [x**2 for x in range(10)]
print(squares)  

#copying a list
a = [1, 2, 3]
b = a.copy() 
print(b)  
