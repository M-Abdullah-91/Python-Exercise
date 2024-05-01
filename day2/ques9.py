# create a function to count the number of vowels in a given string



def count_vowel(sentence):
    count=0
    vowels = 'aeiouAEIOU'
    for char in vowels:
        if char in sentence:
            count+=1
    return count

sentence = input("Enter a sentence: ")
check = count_vowel(sentence)
print(check)