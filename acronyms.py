phrase = input("Enter a phrase")

text = phrase.split()
a = ""
for i in text:
    a = a + i[0]

print(a.upper())