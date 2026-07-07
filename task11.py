# Input
num = int(input("Enter a number: "))

# 1. Sum of Digits
temp = num
sum_digits = 0
while temp > 0:
    sum_digits += temp % 10
    temp //= 10
print("1. Sum of Digits =", sum_digits)

# 2. Reverse a Number
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
print("2. Reverse =", reverse)

# 3. Count Digits
temp = num
count = 0
while temp > 0:
    count += 1
    temp //= 10
print("3. Count of Digits =", count)

# 4. Even or Odd
if num % 2 == 0:
    print("4. Even Number")
else:
    print("4. Odd Number")

# 5. Prime Number
prime = True
if num <= 1:
    prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break

if prime:
    print("5. Prime Number")
else:
    print("5. Not Prime")

# 6. Factorial
fact = 1
for i in range(1, num + 1):
    fact *= i
print("6. Factorial =", fact)

# 7. Factors
print("7. Factors =", end=" ")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print()

# 8. Palindrome
if num == reverse:
    print("8. Palindrome Number")
else:
    print("8. Not Palindrome")

# 9. Armstrong Number
length = len(str(num))
temp = num
armstrong = 0
while temp > 0:
    digit = temp % 10
    armstrong += digit ** length
    temp //= 10

if armstrong == num:
    print("9. Armstrong Number")
else:
    print("9. Not Armstrong")

# 10. GCD (HCF)
a = int(input("Enter First Number for GCD: "))
b = int(input("Enter Second Number for GCD: "))

while b != 0:
    a, b = b, a % b

print("10. GCD (HCF) =", a)