
text = input("enter name :")
print("name :", text)


number1 = float(input("enter number 1:"))
number2 = float(input("enter number 2:"))

print("type of number1:", type(number1))
print("type of number2:", type(number2))

print("sum:", number1 + number2)
print("sub:", number1 - number2)
print("mul:", number1 * number2)
print("div:", number1 / number2)
print("pow:", number1 ** number2)
print("mod:", number1 % number2)

print("sum: {0}".format(
    number1 + number2))  # format parametresinde indexleme 0 dan başladığı için 0 yazdık. format parametresi de string bir ifade de dinamik olarak tip dönüşümü yapmak içindir.
print("number 1: {0} + number 2: {1} = sum: {2}".format(number1, number2, number1 + number2))
print("number 1: {number1} + number 2: {number2} = sum: {sum}"
      .format(number1=number1, number2=number2,
              sum=number1 + number2))  # yukarıdaki örneğin indexlerine argüman göstererek yapıldı.

avg = (number1 + number2) / 2
print("avg:", avg)
print("avg: {0}".format(avg))
print("avg : {avg}".format(avg=avg))


