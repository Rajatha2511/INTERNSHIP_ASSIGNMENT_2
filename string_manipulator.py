#string manipulator
text=input("Enter a string:")#take user input for string
print(f"Original string:{text}")
#convert to uppercase
uppercase_text=text.upper()
print(f"Uppercase string:{uppercase_text}")
#convert to lowercase
lowercase_text=text.lower()
print(f"Lowercase string:{lowercase_text}")
#number of characters with spaces
num_characters_with_spaces=len(text)
print(f"Number of characters with spaces:{num_characters_with_spaces}")
#number of characterstics without spaces
num_characters_without_spaces=len(text.replace(" ",""))
print(f"Number of characters without spaces:{num_characters_without_spaces}")
reverse_text=text[::-1]
print(f"Reversed string:{reverse_text}")#get the reverse of the string
words=text.split()#split the string into words and count the number of words
print(f"Number of words in the string:{len(words)}")
# display first word
if len(words) > 0:
    print("First word:", words[0])
else:
    print("First word: Not available")
# display Last word
if len(words) > 0:
    print("Last word:", words[-1])
else:
    print("Last word: Not available")


