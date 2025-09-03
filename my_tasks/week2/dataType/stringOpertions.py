# # #upper
# # name = "Ada Balogun"
# # print(name.upper())

# # #lower
# # sentence = "PYTHON IS AMAZING"
# # print(sentence.title())
# # print(sentence.lower())

# # #strip to remove white spaces from both ends
# # text = "     Abuja     " 
# # print(text.strip())
# # text = "   Ade   is a  good childtoo"
# # print(text.strip()) 

# # #replaces occurrences of a substring with another substring
# # message = "I love Java"
# # print(message.replace("Java", "Python"))

# # #swapcase switches uppercase to lowercase and viceversa
# # text = "Hello ABEOKUTA"
# # print(text.swapcase())

# # #Lstrip to remove whitespaces or specified characters from only the left side and Rstrip() works for the right side
# # text = "    Nigeria is my country   "
# # print(text.lstrip())
# # print(text.rstrip())

# #splits a string into a list using a seperator (default is space)
# fruits = "mango orange grape apple"
# print(fruits.split())
# text = "one,two,three,four"
# print(text.rsplit(",", 2)) #rsplit splits a list from the right side
# print(text.rsplit(",", 1))

# #splitlines to change strings on \n to list
# lines = "line 1\nline 2\nline 3"
# print(lines.splitlines())

# #join(): To join a list of strings into 1 with a specified separator
# words = ("I", "love", "Python")
# print(" ".join(words))
# text = ("you, are, good")
# print(" ".join(text))
# text = ("y o u", "a r e" "g o od")
# print(" ".join(text))

# #Centers the string within a specified width, padding with spaces or characters
# text = "Python"
# print(text.center(20, "-"))

# #ljust left align  within a specified width, padding with spaces or characters and viceversa for rjust
# text = "python"
# print(text.ljust(8, "*"))
# print(text.rjust(10, "^"))

# #zfill(): Pads a numeric string on the left with zeros until it reaches a given length.
# num = "42"
# print(num.zfill(6))

# #isalpha() Checks if the string contains only letters and viceversa isdigit().
# print("Lagos".isalpha()) 
# print("Lagos12334".isalpha())
print("1234".isdigit()) 
print("Lagos12334".isdigit())

#isalnum(): Checks if the string contains only letters and digits.
print("Python3".isalnum())
print('Python 3'.isalnum())

