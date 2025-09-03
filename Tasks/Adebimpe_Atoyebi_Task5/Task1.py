# Favourite_food1= input("Enter your favourite Nigerian dish 1: ")
# Favourite_food2= input("Enter your favourite Nigerian dish 2: ")
# Favourite_food3= input("Enter your favourite Nigerian dish 3: ")
# dishes = (Favourite_food1, Favourite_food2, Favourite_food3)
# print(dishes)
# print(f"{Favourite_food1}\n{Favourite_food2}\n{Favourite_food3}")

foodlst = []
for i in range(3):
    dish = input(f"Enter you fav dishes {i + 1}: ")
    foodlst.append(dish)
    food = tuple(foodlst)
    print(",".join(food))
    print("\n".join(food))
  

    # print(f"{food[1]} and {food[2]} and{food[-1]}")
