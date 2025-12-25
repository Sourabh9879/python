text = input("Enter a string: ")
vowels = set("aeiouAEIOU")
vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels =", vowel_count, "Consonants =", consonant_count)
