text = input("Enter a text: ")
char = input("Enter character: ")

count = 0

for c in text.lower():
    if c == char.lower():
        count += 1

print("Frequency:", count)

text = "banana"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)