def Q1():
    number = int(input("enter number : "))
    sum = 0
    for i in range(1, number):
        sum = sum + i
    print("sum : {0}".format(sum))


def Q2():
    number = int(input("enter number : "))
    mul = 1
    for i in range(1, number):
        mul = mul * i
    print("mul : {0}".format(mul))


def Q3():
    number = int(input("enter number : "))
    evenCounter = 0
    oddCounter = 0
    for i in range(1, number):
        if i % 2 == 0:
            evenCounter += 1
        else:
            oddCounter += 1
    print("Even Counter: {0}".format(evenCounter))
    print("Odd Counter: {0}".format(oddCounter))


def Q4():
    for i in range(1, 11):
        for j in range(1, 11):
            print("{i} * {j} = {result}".format(i=i, j=j, result=(i * j)))


def Q5():
    number = int(input("enter number : "))
    result = 1
    for i in range(number,1,-1):
        result=result*i
    print("fact : {0}".format(result))

# Q1()
# Q2()
# Q3()
# Q4()
Q5()
