def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] +=1
        else:
            freq[char] = 1
    return freq

text = "hello world"
result = char_frequency(text)

print("Input String:", text)
print("Character Frequency:")
for char, count in result.items():
    print(f"{char}: {count}")