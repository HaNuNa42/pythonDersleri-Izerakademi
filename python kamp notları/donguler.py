# loops - döngüler

for number in range(0, 10):  # başlama ve bitiş parametrelerini yazdık
    print(number)

print("hello world")  # bir tab içeride olsaydı for döngüsünün içinde yazacaktı.

print("*************************")
for number in range(11):  # başlangıç parametresi belirtmeden default olarak başlaması için
    print(number)

print("*************************")
for number in range(1, 11, 2):  # 1den başla 11 e kadar git 2 şer artır
    print(number)

print("*************************")
for number in range(0, 11, 2):
    print(number)

print("*************************")
for number in range(10, 0, -2):
    print(number)