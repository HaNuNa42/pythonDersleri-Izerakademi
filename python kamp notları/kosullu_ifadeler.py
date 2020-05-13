# conditional statements - koşullu ifadeler
number = int(input("enter number : "))

if number == 0:
    print("number is equal to zero")

if number > 0:
    print("number is positive")

if number < 0:
    print("number is negative")

print("***********************")

if number == 0:
    print("number is equal to zero")
elif number > 0:
    print("number is positive")
else:
    print("number is negative")
