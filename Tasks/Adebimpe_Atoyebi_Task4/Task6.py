word = input("Enter a word: ")
print(len(word))
#Checking the word case
if word. isupper(): 
    print("The word is in UPPERCASE")
if word.islower():
    print("The word is in lowercase")
else:
    print("The word is in Titlecase")
print(word[::-1])