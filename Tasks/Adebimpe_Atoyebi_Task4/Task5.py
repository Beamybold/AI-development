namelst = []
scoreLst = []
print("Enter the scores and names of 3 students:")
for i in range(3): # to input names 3 consecutive times
    names = input("enter students names: ")
    scores = int(input(f"Enter score for {names}: ")) # To input scores for each student's name
    namelst.append(names) #to add the list names to the empty list
    scoreLst.append(scores)
print("Name  - Score")
for i in range(3):
    print(f"{namelst[i]} - {scoreLst[i]}") # the [i] alongside each list ensures that each output is printed on a new line since they are in a list 