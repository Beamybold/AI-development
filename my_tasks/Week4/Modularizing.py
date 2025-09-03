# """Modular progamming is a way of writing programs by dividing them into smaller, independent, and reusable parts(modules) instead of writing one long block of code.
# #a module can be a function, a class, or a python file(.py) that performs a specific task
# #they can be combined to build a complete prog.
# #modular programming = breaking big problems into smaller manageable solns
 

# importance of modularity
# 1. READABILITY: breaking code into smaller modules fo easier readability and understanding. This is simply achieved by putting them in different files in a folder.

# 2. REUSABILITY: once a module is created, it can be reused in different programs. this prevent rewritng the same code everytime. eg a function that calc the area of a circle can be used in a sch proj, an engineering proj or a game.

# 3. DEBUGGING AND MAINTENANCE: Incase there is an error, you need to check specific module instead of checking through all the prog. Also, updating or improving one module doesn't break the rest of the prog. EG if you are building a banking appand the payment module in the app has a bug , the user login module is unaffected.

# 4. Teamwork and collaboration: in real-world projects, different developers can work on different modules simultaneously and later combined into the main project EG in building a school mgt system;
# a. one developer handles student recods
# b. another handles teacher records and 
# c. another handles payment system
# All parts are later combined to make one big system.


# 2. FUNCTIONS(1st level of modularity)
# A function is a block of organized, reusable code that performs a single specific task.In python we have 3 types of functions; a. the inbuilt funct
#               b. the user-defined funct
#               c. the lambda funct(a type of user defined function)

# 1. python Built-in functions: they are functions that are preinstalled, you dont need to install any library to use them.
# they include:
#     a. input and output function eg print(to display output) and 
#     b. input() to take user input

#     b. Type conversion functions: int(), float(), str(), bool(), list(), dict(), tuple(), set()....

# c. Mathematical functions: 
#     abs()-absolute value
#     pow(x, y)- x raised to power y
#     round() - round nos to the defined dp
#     min(), max() - find smallest/largest

# d. sequence and collection functions:
#     len()- length of a sequence
#     sum()- sum of elements
#     sorted- sort items
#     enumerate()- track index and value

# e. Utility functions:
#     type()- show the type of an obj(variables, datatypes, data structures, functions, classes)
#     id()- returns unique ID of obj in memory
#     help()- documentation about an obj
# f.  Special built-ins:
#     range()- generates a sequence of nos
#     zip()- combines 2 lists elements in a sequence
#     map()- applies a func to all elements in a sequence
#     filter()- filters elements in a sequence based pn condition """

# #Example: range()
# for i in range (5):
#     print(i) #0, 1, 2, 3, 4

# #zip()
# names = ["Esther", "Precious", "Kennie"]
# scores = [45, 89, 32]
# for n, s in zip(names, scores): 
#     print(n, "scored", s) #Esther scored 45 .....

# #map()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared) #1, 4, 9, 16

# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums) #2, 4

# oddsNum = list(filter(lambda x: x % 2 == 1, nums))
# print(oddsNum) #1, 3

# #Student performance & Feedback system
# #step1: Input student data
# name1 = input("Enter first student name: ")
# score1 = int(input("enter score for " + name1 + ": "))

# name2 = input("Enter the second student name: ")
# score2 = int(input("Enter score  " + name2 + ": "))

# name3 = input("Enter 3rd student name: ")
# score3 = int(input("Enter score  " + name3 + ": "))

# #step2: store in lists
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# #step3: Display data
# print("\nStudent Data:")
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# #step 4: Summary using built-ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)
# print("\nPeformance Summary: ")
# print("Total Score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score:", lowest)

# #step 5: Ranking (using sorted and zip)
# ranked = sorted(zip(scores, names), reverse=True)
# print("\nRanking")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# #Step 6: Check data types
# print("\nData Type Checks:")
# print("Types of names:", type(names))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scores))

# #step 7: Filter passing students (>=50)
# passing = list(filter(lambda s: s >= 50, scores))

# #step 8: Map names to uppercase
# upperNames = list(map(lambda n: n.upper(), names))
# print("Uppercase Names:", upperNames)

# #step 9: Use help() to show documentation of len
# print("\nHelp on len():")
# help(len)

# #ValueError: Invalid literal fo int() with base 10
# """ 
# b. User Defined Function: instead of rewriting codes again and again, we put it inside a function and call anytime it is needed. functions make pogs cleaner, shorter and easier to manage.
# In python, def keyword is used to define a function which we can call whenever we want to use it.
# The function structure:
#    * def function_name(takes in input of what the function will need to wok):
#    * process block(this contains the logic or what you want the function to do)
#    * output block(this contain what you want the function to output using either the 'return' keyword or 'yield' or print() )
# """

# #Defining a function
# def greet():
#     print("Hello, welcome to AI Fellowship!")

# greet() #this is how to call a function when you want to use it

# #Function with an argument - the placeholder
# def greet(name):
#     print("Hello", name, "welcome to python learning!")

# #calling with parameter - the actual name
# greet("class rep")
# greet("Ridwan")

# #When to use return, yield and print() keywords inside a function

# #a. print(): it is used to display ou output not storing so it does not give back a value to use later eg in printing menus, repots, or logs. Eg
# def greet(name):
#     print("Hello", name)
# #Function call
# result = greet("Esther")
# print("Result:", result)

# #b. return: This is used when you want to give back a value. The func ends immediately once it hits return. ie when filing a form and handling it back, the caller now owns the result and can reuse it.
# #You can return when you need the result for further computation or storage eg math calcs, data processing, formatting text etc.
# def add(a, b):
#     return a + b
# #function call
# result = add(4, 6)
# print("The sum is:", result) #The output is differnt from that of print

# #c. yield: This is used for producing a sequence(generators). it works like return  but instead of ending the function, it pauses it and remembers its state. it can be used when working with large data or infinite sequence.
# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i #pause and return i
#         i += 1
# #Using the generator
# for number in count_up_to(5):
#     print(number) 
#Note: the yield output gives all the no one at a time rather than giving all nos at once

# Types of arguments (Function arguments)
# functions can accept different types of arguments depending on how we want to pass data. This makes functions flexible and powerful.
#1. POSITIONAL ARGUMENTS: They are the most common, order matters(They take up value in order that they appear).
# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track, ".")
# #Function call
# introduce("Ngozi", "AI Engineering") #correct order
# #Now test incorrect order
# introduce("AI Engineering", "Ngozi")

# #2. KEYWORD ARGUMENTS: You exxplicitly mention the parameter name when calling the function. Order doesnt matter since python knows which value goes where.
# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track, ".")
# #Function call
# introduce(name = "Ngozi", track = "AI Engineering")
# #Now test incorrect order (Order does not matter)
# introduce(track = "AI Engineering", name = "Ngozi")

# #3. DEFAULT ARGUMENTS: Parameters can be given a default value, even if no value is provided when calling, the default is used
# def introduce(name, track = "AI Engineering"):
#     print("My name is", name) #brings up the name that is used from above without specifying 
#     print("I am learning", track, ".")
# introduce("Paul")
# introduce("Tunji Paul", track = "AI Development") #Specify the default argument which the output takes on now.

# #4. VARYING LENGTH ARGUMENTS: incase we dont know how many arguments will be passed. Python provides 2 special symbols(*)
# #Single asterisk for non-keyword arguments or tuple (*args)
# #Double asterisk for keyword arguments or dict (**kwargs)
#     #a. non-keyword (Tuple): It collectd extra positional arguments into a tuple using * eg  like packing extra clothes into a bag
# def add_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     print("Sum:", total)

# #Function call
# add_numbers(2, 4, 6)
# add_numbers(10, 20, 30, 40, 50)

#     #b. keyword arguments (dict): To collect extra keyword arguments into a dict using **

# def student_details(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)
#     #function call
# student_details(name = "Peter", track = "AI Engineering", interest = "Block Chain")

# #Define student profile function
# #Dont alter the arrangement of the types of arguments used
# def participant_profile(name, age, track="AI Development", *skills, **extra_info):

# # """ generate a profile for a bootcamp participant using different types of argument """
#     profile = f"\n---- Bootcamp Participant Profile ----\n"
#     profile += f"Name: {name}\n"
#     profile += f"Age: {age}\n"
#     profile += f"Track: {track}\n"
# #skills (from *args)
#     if skills:
#         profile += "Skills: " + " ,".join(skills) + "\n"
#     else:
#         profile += "Skills: Not yet specified\n"
# #Extra info from **kwargs
#     if extra_info:
#         profile += "Additional info:\n"
#         for key, value in extra_info.items():
#             profile += f" - {key.capitalize()}: {value}\n"
#     return profile #Return is used to allow for re-using

# #example 1: only positional arguments
# print(participant_profile("peter", 24))

# #Example 2: Adding keyword/default argument
# print(participant_profile("Ridwan", 29, track= "AI Engineering"))

# #Example 3: Adding variable-length positional arguments (*args)
# print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))

# #Example 4: Adding variable-length keyword arguments (**kwargs)
# print(participant_profile(
#     "Sophia", 30, "Cybersecurity",
#     "Networking", "Ethical Hacking", "Python",
#     interest = "Blockchain", city ="Sagamu", phone = "08130164887"
# ))

"""Namespace
It is like a container that holds names(variables, functions, objects) and maps them to the actual data stored in memory. It is like a dict where keys are names and values are objects
Python makes use of it to avoid name conflicts like in a company where different staffs can have the same name but are succintly identify by dept (namespace), so there is no confusion.

Types of Namespaces
1. Built-in namespace - provided by python (len, print, list)
2. Global namespace - Names defined at the top level of a script or module
3. Local namespace - Names created inside a function."""

#Global Namespace
employee = "General Employee"

def IT_department():
    #Local namespace inside IT_department
    employee = "Chris (IT)"
    print("Inside IT Department:", employee)

def Training_department():
    employee = "Chris (Training)"
    print("Inside Training Department:", employee)

print("In Global Namespace:", employee) # Refers to global variable

IT_department() # Uses local variable in IT
Training_department() #uses local variable in Training

#Using a built-in namespace function
print("Length of 'Python':", len("Python"))
#So 'Chris' can exist in more than one namespace without conflict.

"""PE
#Scope defines where in the code a name is accessible. python follows the LEGB Rule(order of search for a variable):
L-Local - Inside the current function
E-Enclosing: Inside any enclosing function(s)
G-Global: At the top level of the script/module
B-Built-in: Python's built-in functions/objects
"""
x = "global x" #Global namespace

def outer():
    x = "enclosing x" #Enclosing Namespace

    def inner():
        x = "local x" #Local Namespace
        print("Inside inner:", x) #Local wins

    inner()
    print("Inside outer:", x) #Enclosing

    outer()
    print("In global:", x) #Global 
#The output is in LEGB order

#Global Keyword: 



    

