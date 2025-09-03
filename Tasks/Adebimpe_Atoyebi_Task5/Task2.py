# bestFriend1= input("Enter your best friend 1: ")
# bestFriend2= input("Enter your best friend 2: ")
# bestFriend3= input("Enter your best friend 3: ")
# bestFriend4= input("Enter your best friend 4: ")
# bestFriend5= input("Enter your best friend 5: ")
# friends = (bestFriend1, bestFriend2, bestFriend3, bestFriend4, bestFriend5)
# print(friends)
# print(friends[::-1])

bestfriend = []
for i in range (5):
    names = input(f"Ënter your bestfriend's name {i + 1}: ")
    bestfriend.append(names)
    bfriend= tuple(bestfriend)
    print(bfriend[::-1])