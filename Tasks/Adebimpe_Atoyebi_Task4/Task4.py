print("enter 5 names: ")
names = input("Enter names: ")
# nameLst = list(names)
nameLst = names.split()#splitting names into a list
# print(nameLst)
nameLst = [name.lower() for name in nameLst]
print(nameLst)
nameLst.sort()
for name in nameLst:
    print(name)

