#List
#using square brackets
emptyList = []
print(emptyList)
fruits = ["apple grape orange pineapple"]
print(fruits)

#using the list() constructor
emptyList2 = list()
print(emptyList2) 
pst2 = list("gj yyeu hduyg yuyeg heue") #list everything icluding the space seperated by ,
print(pst2)

#list of integers, strings, mixed data types
number = [1, 2, 3, 4, 5]
print(number)
fruits = ["apple", "banana", "grape"]
print(fruits)
mixedData = ["Ayo", 25, 5.8, True]
print(mixedData)

#From a string (each character becomes an element)
chars = list("hello")
print(chars)

#from a tuple
myTuple = (10, 20, 30)
listFromTuple = list(myTuple)
print(listFromTuple)

#creating a list with initial elements
#integers
numRange = list(range(10))
print(numRange)

#squares of numbers 0-4
squares = [x**2 for x in range(5)]
print(squares)

#even numbers between 0-10
evens = [x for x in range(11) if x % 2 == 0 ]
print(evens)

#nested list: a list inside list
#matrix-like list
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)
print(matrix[0]) #prints the first matrix
print(matrix[0][1]) #prints the second element from the first bracket
print(matrix[1][0]) #prints the first element from the second bracket

fruits = ["mango", "orange", "apple"]
print(fruits)
print(fruits[0]) #first element

#allow duplicates
items = ["rice", "beans", 'yam', "beans"]
print(items)

#allows element to be modify or altered
numbers = [1, 2, 3, 7]
numbers[1] = 20 #changing element at index 1
numbers[3] = 100
print(numbers)

mixed = [10, "Nigeria", 3.14, True]
print(mixed)
mixed[1] = "umbrella"
print(mixed)

nestedList = [[1, 2], ["a", "b"]]
print(nestedList)
print(nestedList[1][1])

#dynamic size
names = ["ada"]
names.append("Bola")
names.append('ayo')
print(names)




