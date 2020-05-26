"""
Id
make
model
color
year
price
"""


class Vehicle:
    def __init__(self, id=None, make=None, model=None, color=None, year=None,
                 price=None) -> None:  # değerlerimize bir sy girmezsek hata vermesin none olarak kalsın diye onlara none değerini atadık.
        self.id = id
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def setId(self, id):
        self.id = id

    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def setColor(self, color):
        self.color = color

    def setYear(self, year):
        self.year = year

    def setPrice(self, price):
        self.price = price

    def getId(self):
        return self.id

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getYear(self):
        return self.year

    def getPrice(self):
        return self.price

    def calculatePriceWithTax(self):
        return self.price * 1.18

    def __str__(self) -> str:
        return "Id : {id}\n make : {make}\n model : {model}\n color : {color}\n year : {year}\n price : {price}".format(
            id=self.id,
            make=self.make,
            model=self.model,
            color=self.color,
            year=self.year,
            price=self.price
        )
