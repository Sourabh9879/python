text = input("Enter a string: ")
lengths = []

for word in text.split():
    lengths.append(len(word))

print(lengths)
