
# #  Student Bio Data Storage

# student_courses = []
# student_name = input("Kindly enter your name: ")
# student_age = int(input("What's your age?:"))
# student_gender = input("Are you a Male or Female?: ")
# student_courses.append(input("Kindly enter your course: "))

# student_bio_data = {
#     "name": student_name,
#     "age": student_age,
#     "gender": student_gender,
#     "courses": student_courses
# }

# print(f"\nThe Bio-data for student {student_name} is:\nName: \t\t{student_bio_data['name']}\nAge: \t\t{student_bio_data['age']}\nGender: \t{student_bio_data['gender']}\nCourses: \t{student_bio_data['courses']}")

# # Ask for student biodata
# name = input("Enter your name:")
# age = input("Enter your age:")
# gender = input("Enter your gender:")
# course1 = input("Enter your course:")
# course2 = input("Enter your course:")
# course3 = input("Enter your course:")

# courses = [course1,course2,course3]


# biodata = {}
# biodata["Name"] = name
# biodata["Age"] = age
# biodata["Gender"] = gender
# biodata["Course"] = [courses]
# print(biodata)

# print(f"STUDENT BIODATA\nName:\t {name}\n"
# f"Age:\t {age}\nGender:\t {gender}\nCourse:\t {courses}")


# #2
# # #  Super Market Price List
# market_price_list = {}

# items_list = ["Bag", "Jam", "Car", "Mat"]

# for item in items_list:
#     prices = float(input(f"Enter price for {item}: ")) 
#     market_price_list[item] = prices

# for item in market_price_list.keys():
#     print(f"{item}: {market_price_list[item]}" )

# market_price_list.update({"Jam": 100})      # Updating price

# print(f"The updated price in the market list is {market_price_list}")

# # Create an itemlist
# itemlist = []
# item1 = input("Enter the name of Item 1:")
# item2 = input("Enter the name of Item 2:")
# item3 = input("Enter the name of Item 3:")
# itemlist.append(item1)
# itemlist.append(item2)
# itemlist.append(item3)
# print(itemlist)

# # Input the values -prices
# price1 = int(input("Enter the price of Item 1:"))
# price2 = int(input("Enter the price of Item 2:"))
# price3 = int(input("Enter the price of Item 3:"))

# # Add prices to each item
# storeitems = {item1: price1,
#               item2: price2,
#               item3: price3}
# print(storeitems)

# # Print available items
# print(storeitems.keys())
# print(storeitems.values())

# # Display all items and allow user to update 
# for key,value in storeitems.items():
#     print(f"{key}: {value}")

# storeitems.update({item1: price1,})
# print(storeitems.update())


# # 3 Contact Quick Lookup
# names = ("ola", "wale", "ayo")

# phone_no = (+2347012345678, +2349012345678, +2348012345678)

# contact_dict = {name: phone for name, phone in zip(names, phone_no)}

# lookup_name = input("Kindly enter the name you're looking for: ")

# if lookup_name in names:
#     print(f"The corresponding phone number for {lookup_name} is {contact_dict.get(lookup_name)}")
# else:
#     print("Contact not Found!")

# # print(contact_dict)

# Add input
days = ("Day1", "Day2", "Day3", "Day4", "Day5", "Day6", "Day7")
days_ = tuple(days)
# Add user input statement
activity_day1 = input("Please enter an activity:")
activity_day2 = input("Please enter an activity:")
activity_day3 = input("Please enter an activity:")
activities = {activity_day1,activity_day2,activity_day3}


# Pair each activity to a specified day using zip
specific_day = {days[0]}
day_activity = zip(specific_day,activities)
print(f"Days and Activities: {dict(day_activity)}")

# Alternatively
specific_day_activity = {days[0]: activity_day1,
            days[3]: activity_day2,
              days[-1]: activity_day3}
print(specific_day_activity)



