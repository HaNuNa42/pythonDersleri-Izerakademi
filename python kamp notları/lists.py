list1 = []
print(list1)
print(type(list1))

list2 = list()
print(list2)
print(type(list2))

list3 = [3, 12, 22, 33, 55, 10]
print(list3)

list4 = [12, 44, 67, 11, 89, "apple", "orange"]
print(list4)
print(type(list4))
print(len(list4))  # len metodu listenin kaç elemanlı olduğunu verir

print(list4[0])
print(list4[2])
print(list4[5])
print(list4[len(list4) - 1])  # listenin son elemanını almak için yani listeyi tersten okutmak için eksi kullanıyoruz
print(list4[-1])

print("****************************")
print(list4)
print(list4[:4])
print(list4[1:4])
print(list4[3:])
print(list4[::2])  # listeyi ikişer atlayarak  verir
print(list4[::-2])  # listeyi tersten ikişer ikişer tersten verir

print("****************************")
numberList1 = [1, 2, 3, 4, 5, 6]
numberList2 = [89, 12, 55, 78, 32, 43]
print(numberList1)
print(numberList2)
print(numberList1 + numberList2)
numberListResult = numberList1 + numberList2
numberListResult = numberListResult + ["apple"]
print(numberListResult)

print("****************************")
numberListResult[1] = 22
print(numberListResult)
numberListResult[-1] = "orange"
print(numberListResult)

numberListResult[:2] = [20, 40]
print(numberListResult)

print(numberListResult * 3)

print("***************************")
numberListResult.append("english")  # append metodu listeye eleman eklemek için
numberListResult.append("german")
print(numberListResult)

print("****************************")
numberListResult.pop()
print(numberListResult)
numberListResult.pop(2)  # pop metodu 2 indexine sahip olan elemanı listeden çıkarmak için kullanılır
print(numberListResult)

print("****************************")
numberListResult.append(20)
print(numberListResult)
print(numberListResult.count(20))  # count metodu listede istediğimiz elemanın ka tane olduğunu gösterir.

print("****************************")
numberListResult.insert(1, 98)
print(numberListResult)

print("****************************")
numberListResult.remove("orange")  # remove metodu listedeki elemanı siler
print(numberListResult)

print("****************************")
numberListResult2 = [1, 2, 67, 7, 213]
numberListResult.extend(numberListResult2)  # extend metodu listenin sonuna yeni oluşturduğumuz diğer listenin sonuna ekler
print(numberListResult)

print("****************************")
numberListResult.reverse()  # reverse metodu listenin tersini alır.
print(numberListResult)

print("****************************")
numberListResult.clear()  # clear metodu bütün listeni elemanlarını siler
print(numberListResult)

del numberListResult
numberListResult