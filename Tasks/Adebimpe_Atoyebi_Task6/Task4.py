votersName = set()
for i in range (4):
    names = input(f"enter voters name {i +1}: ").title()
# name2 = input("enter voters name2: ")
# name3 = input("enter voters name3: ")
# name4 = input("Enter your name4:")
# names = (name, name2, name3, name4)
    votersName.add(names)
    # print(votersName)
while True:
    added_name = input("enter your name: ").title()
  
    if added_name in votersName:
        print(f"Warning:{added_name} cannot register twice.")
    elif added_name.isdigit():
            print("Name can not be numeric")
    else:
        print(f"{added_name} You have successfully register.")
        votersName.add(added_name)
        print(votersName)
    
        exit = input("Press 'Done' to exit: ").title()
        if exit == "Done":
            print("Registration complete!")
            break
        else:
            continue

print(f"The total number of unique voters are {len(votersName)}")