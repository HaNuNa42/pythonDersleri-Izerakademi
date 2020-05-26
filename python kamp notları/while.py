# while

number = 0
while number < 6:
    print(number)
    number += 1
    if number == 5:
        break
    if number == 3:
        continue
    print("hello world")

print("************************")

for number in range(0,6):
    if number == 5:
        break
    if number == 3:
        continue
    print("hello world")