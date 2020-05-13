limit = int(input("enter number:"))
for number in range(1, limit):
    if number % 2 ==0:
        print("even number: {0} ".format(number))
    else:
        print("odd number: {0}".format(number))

