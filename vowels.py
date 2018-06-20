vowels = ['a','e','i','o','u']
words = input("Provide a word to search for vowels:")
found = []
for letter in words:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vol in found:
    print(vol)