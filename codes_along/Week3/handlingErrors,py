# #Handling errors in python
# #syntax errors: this happens when python interpreter cannot understand ones code because it is against python grammar rules
# #a. IndentationError: Incorrect spacing
# for i in range(3):
# print(i)   # Wrong indentation use tab to correct

# #missing colon/parenthesis error
# if 5 > 3 #missing column
# print("Hello")

# #Invalid syntax - General grammar mistakes
# print "Hello" #Missing parenthesis
# #To fix just double check python grammar, colons, parentheses, and indentation

#Runtime errors(exceptions): This program is syntactically correct, but an error occurs while it is running. They can be handled with try, except, and finally
#a. ZeroDivisionError reports when you divide by zero
# x = 10/0

#b. NameError occurs when a variable is used before defining it
# print(age)

#c. TypeError reports when a wrong data type is inputted in an operation
# result = "10" + 5 #string + int not allowed

#d. ValueError means an invalid zvalue has been inputted for a function
# number = int("abc") #cannot convert str to int

#e. IndexError means you are trying to access list index out of range
# fruits = ["apple", "banana"]
# print(fruits[3]) #index out of range because it ends on [1]

#f. KeyError occur when accessing a dictionary with a missing or unavailable key.
# data = {"name" : "Ada"}
# print(data["age"]) 

# #g. FileNotFoundError means the file does not exist
# f = open("missing.txt")

#Handling runtime errors
#The keywords used in handling errors to preventt progs from crashing are:
#a. try block which is used to test for errors
#- it is used to wrap code that might raise an error
#- if no error occurs python skips the except block
# try:
#     x = 10 / 2
# print("Result:", x)

#The except block runs if an error occurs
#It defines what to do if an error occcurs inside try
#It can catch specific errors or all errors

# #This is a specific exception
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# #This is a case of multiple exception
# try:
#     number = int("abc") #ValueError
#     result = number / 0     #ZeroDivisionEror

# except ValueError:
#     print("Invalid conversion to integer")

# except ZeroDivisionError:
#     print("Cannot divide by zero.")


# #the finally block always un whethe an error occured or not.
# #It is useful for cleanup tasks (e.g closing files and releasing resouces)

# try: 
#     f = open("sample.txt", "r")
#     content = f. read() 

# except FileNotFoundError:
#     print("File not found.")

# finally:
#     print("Closing file if it was opened,")

# #example
# balance = 5000 #(starting balance)
# print("Welcome to the ATM")
# amount  = input("Enter amount to withdraw: ")

# try:
#     amount = float(amount)
#     #convert input to number

#     if amount > balance:
#         raise ValueError("Insufficient funds.")

#     balance -= amount
#     print("Withdrawal successful. New balance: ₦", balance)

# except ValueError as e:
#     print("Error:", e)

# except Exception as e:
#     print("Unexpected error:", e)

# finally:
#     print("Transaction session closed.")

# """if user enters 2000; withdrawal successful. New balance: ₦3000.0
# Transaction session closed.

# if user enters 6000 
# - Error: Insufficient funds.
# - Transaction session closed.
# if user enters abc
#  - Error: could not convert string to float: 'abc'
#  - Transaction session closed."""

#semantic errors are mostly logic mistakes
#the code runs without crashing but the output is logically wrong
#hardest to detect because the interpeter sees no error
#They are not officially exceptions in python but are real mistakes programmers make when the logic is wrong.

#Wrong condition in logic
age = 18
if age > 18: #Should be >=
    print("Eligible to vote") 
else:
    print("Not eligible")

#output: Not eligible (wrong result)

#Wrong Formula/computation
length = 10
width = 5
area = length + width #(instead of multiplication)
print("Area:", area)

#Wrong variable usage
marks = [70, 80, 90]
total = marks[0] * marks[1] * marks[2]
#wrong, should be sum
print("Total:", total)

#To fix semantic errors carefully review logic, test with multiple cases, use debugging or print statements







