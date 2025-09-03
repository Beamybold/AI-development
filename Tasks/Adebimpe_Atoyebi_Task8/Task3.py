#online store calculator
items = ["book", "pen", "bag", "flask", "cloth"]
prices = [200, 600, 3556, 355, 100]
pickedItems = ["book", "pen", "cloth"]
cartTotal = 0
cartTotal += prices[0] #using an assignment operator to add the prices of some items
cartTotal += prices[1]
cartTotal += prices[4]
# print(cartTotal)
print(f"Item: {pickedItems}\nTotal price: ₦{cartTotal}")