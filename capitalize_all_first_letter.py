# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# Ask user to input string
string = input("Enter the string: ")

# Print input in title casing
words = string.split()

title_case_string = " ".join(
    (chr(ord(word[0]) - 32) if 'a' <= word[0] <= 'z' else word[0]) +
    "".join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in word[1:])
    for word in words
)

print("Title case string:", title_case_string)