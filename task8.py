num = int(input("Enter a number: "))
original = num
length = len(str(num))
total = 0
while num > 0:
    digit = num % 10
    total = total + (digit ** length)
    num = num // 10
if total == original:
    print(original, "is an Armstrong Number")
else:
    print(original, "is not an Armstrong Number")