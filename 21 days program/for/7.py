sentence = input("Enter a sentence: ")
counts = {}

for word in sentence.split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
