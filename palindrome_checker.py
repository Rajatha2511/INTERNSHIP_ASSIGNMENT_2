# take a user input for a word or a number
text=input("Enter a word or a number:")
processed_text=text.strip().lower() #convert the text to lowercase if it is a word
print("processed text:",processed_text)
print("converting the input to lowercase,(ifword)")
#reverse the processed text
reversed_text=processed_text[::-1]
print("reversed text:",reversed_text)
#compare
if processed_text==reversed_text:
    print("The text is a palindrome")
else:
    print("The text is not a palindrome")


