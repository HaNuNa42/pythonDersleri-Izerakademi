def sum(number1, number2): # def parametresi bir değişken adı tanımlayıp parantez içinde de dışarıdan alacağı iki değeri de tanımladığımız bir metotdur. bir nevi metod oluşturmak için kullanılır.
    result = number1 + number2
    return result


def sub(number1, number2):
    result = number1 - number2
    return result


def mul(number1, number2):
    result = number1 * number2
    return result


def div(number1, number2):
    result = number1 / float(number2)
    return result


sumResult = sum(10, 20)
print("sum: {0}".format(sumResult))
print("*****************")
subResult = sub(20, 10)
print("sub: {0}".format(subResult))
print("*****************")
mulResult = mul(10, 20)
print("mul: {0}".format(mulResult))
print("*****************")
divResult = div(10, 7)
print("div: {0}".format(divResult))
