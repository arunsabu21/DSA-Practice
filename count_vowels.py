# Count how many vowels (a, e, i, o, u) are in the string

text = "hello world"
vowels = "aeiou"

# Iterate through each character and count if it's a vowel

count = sum(1 for char in text if char.lower() in vowels)

print("Text:", text)
print("Number of vowels:", count)