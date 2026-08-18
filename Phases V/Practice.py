# # Question : 1 Slicing ka use karke reverse karo.
# word = "Programming"
# print (word[::-1])

# # Question : 2  for loop ka use karke reverse karo.
# word = "Akash"
# reverse = ""

# for char in word:
#     reverse = char + reverse

# print(reverse)


# # Question 3 - Interview Challenge
# word = "madam"
# reverse = ""
# for char in word:
#   reverse = char + reverse
# if word == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")



# # Question : - Final Challenge
# word = "level"
# reverse = ""
# for char in word:
#     reverse = char + reverse
# if word == reverse:
#     print("Palindrome")
# else :
#     print("No Palindrome")            


text = "Python is very easy"

vowel_count = 0
space_count = 0

for char in text.lower():
    if char in "aeiou":
        vowel_count += 1

for char in text:
    if char == " ":
        space_count += 1

print("Vowels:", vowel_count)
print("Spaces:", space_count)


text = "Python is very easy"

consonant_count = 0

for char in text.lower():
    if char.isalpha() and char not in "aeiou":
        consonant_count += 1

print(consonant_count)