# input statement for the customer's name
# input the name to give us the input
# define order 
# define the customers specific order with input staement (order2)
# input the customers final order

name = input("Enter your name: ")
C = "Customer"
A = "Attendant"
print( "Hello,")
print({A}, ":Good day! Miss", name)
order = input("What the customers would love to have: ")
print({C}, ":Thank you, do you have", order, "?" )
print({A}, ":Miss", name, "what type of", order, "do you prefer?")
print("We have white rice, jollof rice , fried rice and coconut rice.")
order2 = input("What the customer want: ")
print("I would love to have", order2)
print("Okay, what will you love to accompany it with")
finalOrder = input("Enter protein and drink: ")
print("I am cool with", finalOrder)
print("Give us 3 minutes to get you the ",  order,  "with", finalOrder)