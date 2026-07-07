string = "hi hello raju"
vowels = ""
consonants = ""
for ch in string.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += ch
        else:
            consonants += ch
print("Vowels     :", vowels)
print("Consonants :", consonants)