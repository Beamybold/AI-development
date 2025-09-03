# #define variables with different data types

# name = "Ade"            #string 
# number =[3, 4, 8]            #integer
# pi = 3.14               #float


# int()
# float()
# str()
# bool()

# #converting input to question mark
# age = int(input("Enter your age: "))
# print(f"Your age will be {age + 20} in the next 20 years.")

# #Simple calculator
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# sum_result = num1 + num2
# print(f"The sum of {num1} and {num2} is {sum_result}.")

#USSD code
USSD = int(input("USSD code: "))
Data_plans = int(input("Enter to buy data: "))
Biz_plans= int(input("Enter to initiate : "))

print(f"Dial {USSD} to access MTN self-service centre,\n{Data_plans} for data plans")