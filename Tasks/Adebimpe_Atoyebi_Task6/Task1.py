#Ask the user to enter 5 favourite fruits. Store them in a set and display the set.
print("Enter your 5 favourite fruits:")
# for i in range(5):
fruits = input("Enter the name of 5 fruit sep. by space: " ).split()
# fruit1 = input("enter fruit1: ")
# fruit2 = input("enter fruit2: ")
# fruit3 = input("enter fruit3: ")
# fruit4 = input("enter fruit4: ")
# fruit5 = input("enter fruit5: ")
# fruits = set([fruit1, fruit2, fruit3, fruit4, fruit5])
fruits = set(fruits)
print(fruits)


