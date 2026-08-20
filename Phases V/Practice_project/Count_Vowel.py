text = input("Enter a text: ")

vowel_count = 0

for char in text.lower():
    if char in "aeiou":
        vowel_count += 1

print("Vowels:", vowel_count)