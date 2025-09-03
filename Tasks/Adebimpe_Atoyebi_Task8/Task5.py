#- Create a dictionary called store with items and their available quantities. Example:
store = {"Book" :  12, "Gun" : 18, "Pen" : 23, "Keys" : 76}
#Ask the user to input the item they want to buy (e.g., "Pen").
item = input("enter the item you want to buy: ").title()
Quantity = int(input(f"Enter the quantity of {item} you want to buy: "))
print(f"Before Purchase: {store}")
#Use the assignment operator -= to update (reduce) the item quantity in the dictionary.
store[item] -= Quantity
print(f"After Purchase: {store}")


