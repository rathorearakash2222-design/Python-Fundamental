# #    Day - 5 : Count Characters
# text = "banana"

# print(text.count("a"))

# text = "programming"

# print(text.count("m"))
# print(text.count("g"))
# print(text.count("p"))

# text = "python is easy and python is powerful"

# print(text.count("Z"))

# text = "banana"
# count = 0

# for char in text:
#     if char == "a":
#         count += 1

# print(count)


# # Vowels Count 
# text = "programming"
# count = 0

# for char in text:
#     if char in "aeiou":
#         count += 1

# print(count)

# Uppercase 
text = "Akash"
count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print(count)

# Space Count 
text = "Akash Rathore"
count = 0

for char in text:
    if char == " ":
        count += 1

print(count)

text = "Python is very easy"

consonant_count = 0

for char in text.lower():
    if char.isalpha() and char not in "aeiou":
        consonant_count += 1

print(consonant_count)