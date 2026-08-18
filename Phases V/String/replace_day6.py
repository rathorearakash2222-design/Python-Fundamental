#string.replace(old, new)
text = "I like Java"

print(text.replace("Java", "Python"))

# Split() - string Ko Parts/List main Todna
text = "Akash Rathore"

words = text.split()

print(words) 

#join() - List Ko String main jodna

words = ["Akash", "Rathore"]

name = " ".join(words)

print(name)

text = "Python is very easy"

words = text.split()

result = "-".join(words)

print(result)