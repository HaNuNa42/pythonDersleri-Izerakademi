dictionaryList = {}
print(type(dictionaryList))
print(dictionaryList)

dictionaryList = dict()
print(type(dictionaryList))
print(dictionaryList)

dictionaryList = {"Lang1": "English", "Lang2": "German", "Lang3": "Spanish"}
print(dictionaryList)

print("Value of Lang1: {0}".format(dictionaryList["Lang1"]))
print("Value of Lang2: {0}".format(dictionaryList["Lang2"]))
print("Value of Lang3: {0}".format(dictionaryList["Lang3"]))
# dictionaryList["Lang3"] = "Greek"
dictionaryList["lang4"] = "Spanish"
print(dictionaryList)

print("*************Nested Dictionary**************")
dictionaryList = {
    "Plates": {"Plate1": 35, "Plate2": 6, "Plate3": 34},
    "Cities": {"City1": "Izmir", "City2": "Ankara", "City3": "Istanbul"}
}
print(dictionaryList)
print("*************Plates**************")
print("Plates : {0}".format(dictionaryList["Plates"]))
print("Plates 1: {0}".format(dictionaryList["Plates"]["Plate1"]))
print("Plates 2: {0}".format(dictionaryList["Plates"]["Plate2"]))
print("Plates 3: {0}".format(dictionaryList["Plates"]["Plate3"]))

print("*************Cities**************")
print("Cities : {0}".format(dictionaryList["Cities"]))
print("Cities 1: {0}".format(dictionaryList["Cities"]["City1"]))
print("Cities 2: {0}".format(dictionaryList["Cities"]["City2"]))
print("Cities 3: {0}".format(dictionaryList["Cities"]["City3"]))

print("*************Get - Plates**************")
print("Plates : {0}".format(dictionaryList.get("Plates")))
print("Plate 1: {0}".format(dictionaryList.get("Plates").get("Plate1")))
print("Plate 2: {0}".format(dictionaryList.get("Plates").get("Plate2")))
print("Plate 3: {0}".format(dictionaryList.get("Plates").get("Plate3")))

print("*************Get - Cities**************")
print("City : {0}".format(dictionaryList.get("Cities")))
print("City 1: {0}".format(dictionaryList.get("Cities").get("City1")))
print("City 2: {0}".format(dictionaryList.get("Cities").get("City2")))
print("City 3: {0}".format(dictionaryList.get("Cities").get("City3")))

print("**************************")
productList = {
    "1": {"ProductName": "Computer",
          "ProductDescription": "Computer test decsription",
          "Quantity": 10,
          "Price": 5700,
          "Specification": {"Cpu": "9700K",
                            "Motherboard": "Asus Z390",
                            "Ram": "16GB"}},
    "2": {"ProductName": "Macbook Pro",
          "ProductDescription": "Macbook Pro test decsription",
          "Quantity": 20,
          "Price": 15700,
          "Specification": {"Cpu": "9900K",
                            "Motherboard": "Asus Z390",
                            "Ram": "32GB"}},
}
print("Product 1 : {0}".format(productList.get("1")))
print("ProductName : {0}".format(productList.get("1").get("ProductName")))
print("Quantity : {0}".format(productList.get("1").get("Quantity")))
print("Price : {0}".format(productList.get("1").get("Price")))
print("Specification : {0}".format(productList.get("1").get("Specification")))
print("Specification => CPU : {0}".format(productList.get("1").get("Specification").get("Cpu")))
print("Specification => Motherboard : {0}".format(productList.get("1").get("Specification").get("Motherboard")))
print("Specification => Ram : {0}".format(productList.get("1").get("Specification").get("Ram")))

print("*********************************************************")

print("Product 2 : {0}".format(productList.get("2")))
print("ProductName : {0}".format(productList.get("2").get("ProductName")))
print("Quantity : {0}".format(productList.get("2").get("Quantity")))
print("Price : {0}".format(productList.get("2").get("Price")))
print("Specification : {0}".format(productList.get("2").get("Specification")))
print("Specification => CPU : {0}".format(productList.get("2").get("Specification").get("Cpu")))
print("Specification => Motherboard : {0}".format(productList.get("2").get("Specification").get("Motherboard")))
print("Specification => Ram : {0}".format(productList.get("2").get("Specification").get("Ram")))

print("**********Pop***********")
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))
print(squares)

print("**********PopItem***********")
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.popitem())
print(squares)

print("**********Clear***********")
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
squares.clear()
print(squares)

print("**********del***********")
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
del squares[4]
print(squares)

print("**********items***********")
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.items())

print("**********set default***********")
person = {"name": "hatice", "age": 25}
age = person.setdefault("age", 40)
print("Peron : {person}".format(person=person))
print("age: {age}".format(age=age))

person = {"name": "hatice"}
age = person.setdefault("age", 40)
print("Peron : {person}".format(person=person))
print("age: {age}".format(age=age))

print("**********update***********")
person = {"name": "hatice", "age": 60}
person.update({"name": "nur"})
print("Peron : {person}".format(person=person))

print("**********values***********")
print("values: {values}".format(values=person.values()))  # values değerlerin listesini verir

print("**********keys***********")
print("keys: {keys}".format(keys=person.keys()))  # keys değerlerin listesini verir

print("*******************************")
people = {
   1: {"name": "hatice", "age": 17},
   2: {"name": "nur", "age": 43},
   3: {"name": "ayşe", "age": 20}
}
for key, value in people.items():
    print("person key : {0}".format(key))
    for k in value:
        print("{k} : {v}".format(k=k, v=value[k]))
    print("********")
