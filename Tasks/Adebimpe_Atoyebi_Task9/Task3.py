"""Word Analyzer**
- Ask the user to input a word.
- Print the length of the word.
- Check if it is all uppercase, all lowercase, or title case."""

word = input("Enter a word: ")
# print(len(word))
#Checking the word case
if word. isupper(): 
    print("The word is in UPPERCASE")
elif word.islower():
    print("The word is in lowercase")
else:
    print("The word is in Titlecase")