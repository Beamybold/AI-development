#creating tuple
#using () for tuple with multiple items
fruits = ("apple", "banana", "cherry")
print(fruits)  # ('apple', 'banana', 'cherry')

#without ():tuple packing
numbers = 1, 2, 3
print(numbers)  # (1, 2, 3)
print(type(numbers))

#single item tuple must include ,
single_item = ("apple",)
print(single_item)       # ('apple',)
print(type(single_item)) # <class 'tuple'>

#Using the tuple() constructor
fruits_list = ["apple", "orange", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)  # ('apple', 'banana', 'cherry')

#characteristics
#Ordered
colors = ("red", "green", "blue")
print(colors[0])  # red
print(colors[1])

# # Immutable ( uncomment and run. This will cause an error)
# colors[1] = ("yellow",)  #  TypeError because it does not allow change  after creation
# print(colors[1])

# Allow duplicates
numbers = (1, 2, 3, 2, 3)
print(numbers)  

#mixed data types
# Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)  # ('apple', 3, True, 5.6)

#Tuple operations
#1 indexing
fruits =  ("apple", "orange", "banana", "mango", "cherry")
print(fruits[4])

#2 Slicing
print(fruits[0:2])   
print(fruits[::-1])  #arrange from the last to the front

#3 Concatenation: joins together
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)  # (1, 2, 3, 4)

#4 Repetition
nums = (1, 2)
print(nums * 3)  # (1, 2, 1, 2, 1, 2)


#5 Membership
fruits = ("apple", "box", "1", "banana", "cherry")
print("banana" in fruits)  # True
print("grape" not in fruits)  # True

#6 Iteration
for fruit in fruits:
    print(fruit)

#working with tuples:convert to a list, modify and convert back
#unpacking tuples
person = ("John", 25, "Nigeria",)
name, age, country = person
print(name)
print(country)

#Tuple methods: they are just 2
# dont count() and dot index()
numbers = (1, 2, 2, 3, 4)
print(numbers.count(2))  # 2  (counts occurrences of 2)
print(numbers.index(3))  # 3  (position of first occurrence of 3)

#converting between list and tuple
# Tuple to List
t = (1, 2, 3)
lst = list(t)
lst.append(4)
lst.append(67)
print(lst)  # [1, 2, 3, 4, 67]
#list back to tuple
t = tuple(lst)

#built-in functions with tuples
nums = (4, 1, 7, 3, 7)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))



