word = input("Enter a word: ")

reverse_word = word[::-1]

if word==reverse_word:
    print(f"{word} is palindrome")
else:
    print(f"{word} is not palindrome")
