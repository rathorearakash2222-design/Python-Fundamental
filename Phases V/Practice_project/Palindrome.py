word = input("Enter a word: ")

reverse = ""

for char in word:
    reverse = char + reverse

if word.lower() == reverse.lower():
    print("Palindrome")
else:
    print("Not Palindrome")