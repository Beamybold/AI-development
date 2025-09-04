# #Control flow in python
# #1. Conditional Statements: if statement
# age = 20
# if age >= 18:
#     print("You are eligible to vote")
# #if-else statement provides two alternative paths
# wallet = 400
# price = 500
# if wallet >= price:
#     print("Purchase successful")
# else:
#     print("Insufficient balance")
# #if-elif-else statement for multiple conditions
# score = 85
# if score >= 70:
#     print("Grade A")
# elif score >= 50:
#     print("Grade B")
# else:
#     print("Grade C")

# #Nested if 
# age = 19
# citizen = True
# if age >= 18:
#     if citizen:
#         print("You can vote")
#     else:
#         print("You must be a citizen to vote")   
# else:
#     print("Too young to vote")


# #2 Loop: for loop: used to iterating over a sequence (picking one by one)
# #LIST: Iterates through each element in a list
# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(f'I like {fruit}')

# #TUPLE iterates through elements in a tuple, it is immutable unlike list
# coordinates = (0.3464, -0.47557, 0.587)
# for point in coordinates:
#     print(f"Point: {point}")

# #DICT iterates through each element (Key : Element)
# student =  {"name" : "Tunde", "Age" :  16, "Grade" : "A"}
# for key, value in student.items():
#     print(f"{key} : {value}")

# #STRING iterates through each element in a string in form of sequences of characters
# word = "PYTHON"
# for char in word:
#     print(char)


#WHILE loop is condition-based, used to repeatedly execute a block of code as long as a given condition is true otherwise it stops

## Documenting my thoughts##
# Let the loop start with count = 3
# Let it keep printing until count is greater than 15 adding 2 per number
# Let the loop terminate when the condition is no longer true

# count = 3
# while count <= 15:
#     print("Number:", count)
#     count += 2

#incrementing with "while"
# num = 10
# while num <= 100:
#     print(num, end=" ") #start printing from 10 and end on 100 adding 10 to each count
#     num += 10

# #decrementing with "while"
# timer = 100
# while timer >= 10:
#     print("Countdown:", timer)
#     timer -= 10

#used to confirm right password input
# password = ""
# while password != "python123":
#     password = input("Ënter your password: ")
# print("Access granted")

#while true
    #code block
    #must include a break statement to stop
# while True:
#     name = input("Enter your name (type 'exit' to quit): ")
#     if name.lower() == 'exit':
#         print('Goodbye!')
#         break #used in chatlike apps, forms or data entry progs where users may input multiple times until they decides to stop.
#     print(f'Hello, {name}')

#     #loop ctrl statements (break, continue and pass)
#     #BREAK: To stop a loop immediately the set condition is met
#     for num in range(1, 20): 
#         if num == 5:
#             break
#         print(num) 

#CONTINUE skips the current iteration and moves to the next one. it is used to ignore some value but keep the loop running
# for num in range (1, 6):
#     if num == 3: # This is to skip 3
#         continue
#     print(num)
# it is used to skip invalid data, ignore unwanted characters eg spaces in a string 

#PASS does nothing, it is used if code hasnot been written but you want to keep the structure
# for num in range(1, 6):
#     if num == 3:
#         pass
#     else:
#         print(num)
#this is used in writing code structure to fill later.
#placeholders in class/mtd definitions
#temporary disable parts of code

# while True:
#     print("Menu")
#     print("1. Say Hello")
#     print("2. Say Goodbye")
#     print("3. Exit")

#     choice = input("Choose an option: ")

#     if choice == "1":
#         print("Hello")
#     elif choice == "2":
#         print("Goodbye")
#     elif choice == "3":
#         print("Exiting program.....")
#         break
#     else:
#         print("Invalid choice. Try again.")

# while True:
#     age = input("Enter your age: ")
#     if age.isdigit():
#         print("Your age is: ") 
#         break
#     else:
#         print("Invalid input. Please emter a number.") #This is used fo validation

# secret = "python"
# while True: 
#     guess = input("Guess the secret word: ")
#     if guess.lower() == secret:
#         print("Correct! You guessed the right word.")
#         break
#     else:
#         print("Wrong! Try again.")



# balance = 1000
# while True:
#     print("\nATM Menu:")
#     print("1. Check Balance")
#     print("2. Withdraw")
#     print("3. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         print(f"Your balance is: {balance}")
#     elif choice == "2":
#         amount = int(input("Enter withdrawal amount: "))
#         if amount <= balance:
#             balance -= amount
#             print(f"Withdrawal successful. New balance: {balance}")
#         else:
#             print("Insufficient funds.")
#     elif choice == "3":
#         print("Thank you for using our ATM. Goodbye!")
#         break
#     else:
#         print("Invalid option. Try again.")
