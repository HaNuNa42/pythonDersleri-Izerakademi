limit = int(input("enter number:"))
sum = 0
for number in range(1, limit):
    sum = sum + number
    sum += number
    print("number:{0}".format(number))
    print("sum:{0}".format(sum))

print("sum:{0}".format(sum))