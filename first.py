# Ask the user to enter a word
word = input("Enter a word: ")

# Reverse the word
reversed_word = word[::-1]


# Check if it's a palindrome
if word == reversed_word:
    print("This is a palindrome!")
else:
    print("This is not a palindrome.")
