word = input("Enter a word to check: ")

rev_word = word[::-1]

if word == rev_word:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")