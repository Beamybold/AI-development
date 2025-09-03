#6 print to check the substring in a string
text = "I am learning python to become an AI developer"
print("python" in text)

# #7 Reversing astring using join and reverse function
# word = "capital"
# word = "".join(reversed(word))
# print(word)

# #8  removing extra spaces in a string
# state = " Adamawa       "
# print(state.strip()) 

#9 printing out vowels from a sentence
sentence = input("Enter a sentence: ")
vowels = "aeiou".lower()

count = 0
for char in sentence:
        if char in vowels:
                count += 1
print(f"There are {count} vowels in the sentence \"{sentence}\".")

# sentence = input("Enter a long sentence: ").lower()
# consonants = "bcdfghjklmnpqrstvwxyz"

# count = 0
# for char in sentence:
#     if char in consonants:
#         count += 1
# print(f"They are {count}")



# #10 convert a string to interger and * 2
# num = "1234"
# intNum = int(num)
# operation = intNum * 2
# print(f"{intNum} multiply by 2 is {operation}")


