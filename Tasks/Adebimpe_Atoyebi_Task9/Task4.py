"""Create a Unique Voters Registration System**

- Ask for voter names and store in a set.

- If a voter tries to register twice, display a warning.

- After registration, display the total number of unique voters.. """


votersName = set()
for i in range (4):
    names = input(f"enter voters name{i +1}: ")
# name2 = input("enter voters name2: ")
# name3 = input("enter voters name3: ")
# name4 = input("Enter your name4:")
# names = (name, name2, name3, name4)
    votersName.add(names)
    # print(votersName)

    name = input("enter your name: ")
for name in votersName: #to check if name is in votersname
    if name == votersName:
        print(f"Warning:{name} cannot register twice.")
    break
else:
    print(f"{names} You have successfully register.")
    print("Registration complete!")
    print(f"The total number of unique voters are {len(votersName)}")