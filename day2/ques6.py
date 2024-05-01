import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    for char in alphabet:
        if char not in sentence.lower():
            return False
        
    return True

sentence = input("Enter a sentence: ")
if is_pangram(sentence) == True:
    print('sentence is pangram')
else:
    print("sentence is not pangram")
