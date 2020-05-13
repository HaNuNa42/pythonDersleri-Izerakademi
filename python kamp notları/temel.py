# variables - degiskenler
# integer numbers - tam sayilar

number = 5
print("number:", number)
print(type(number))

# floating numbers - ondalikli sayilar
number = 5.7
print("number:", number)
print(type(number))

# integer numbers - tam sayilar
number = 6
print("number:", number)
print(type(number))

# string - metinsel ifadeler
# camelcase => firstName gibi birinci kelimenin baş harfi küçük ile başlayıp ikinci kelimenin harfi büyük başlaması durumudur. => kullandığı diller; kotlin, java, python
# pascalcase => FirstName => c#

firstName = "hatice"
lastName = "nur"
print("firstName:", firstName)
print("lastName: ", lastName)
print("type of firstname", type(firstName))
print("type of lastname", type(lastName))

# basic casting - basit tip dönüşümü
number = 10.6
print("number:", number)
print("type of number:", type(number))

newNumber = int(number)
print("new number:", newNumber)
print("type of number", type(newNumber))

newNumber = str(number)
print("new number:", newNumber)
print("type of number", type(newNumber))

# bool - mantıksal yapılar
isCorrect = True
print("is correct: ", isCorrect)
print("type of number", type(isCorrect))

number1 = 4
number2 = 6
number3 = 15
print(number1, number2, number3)
print(number1, number2, number3, sep="+")  # sep aralarına ayraç koyan bir paremetre
print(number1, number2, number3, sep="\n")
print(number1, number2, number3, sep="+", end="=")  # end ise sonuna koyacağımız bir ayraç veya ifadede kullanılır.
print(number1 + number2 + number3)
print("sum:" + str(number1 + number2 + number3))
print("sum:", number1 + number2 + number3)
