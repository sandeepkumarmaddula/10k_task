#given number is positive or not
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
#Check whether a character is uppercase or lowercase
ch = input("Enter a character: ")
if 'A' <= ch <= 'Z':
    print("Uppercase")
elif 'a' <= ch <= 'z':
    print("Lowercase")
else:
    print("Not an alphabet")
#Pass or Fail (6 Subjects)
s1 = int(input("Enter Subject 1 marks: "))
s2 = int(input("Enter Subject 2 marks: "))
s3 = int(input("Enter Subject 3 marks: "))
s4 = int(input("Enter Subject 4 marks: "))
s5 = int(input("Enter Subject 5 marks: "))
s6 = int(input("Enter Subject 6 marks: "))
if s1 >= 35 and s2 >= 35 and s3 >= 35 and s4 >= 35 and s5 >= 35 and s6 >= 35:
    print("Pass")
else:
    print("Fail")