from oop.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, id=None, make=None, model=None, color=None, year=None, price=None, airSuspension=None) -> None: # farklı olan özelliği de buraya ekleriz
        super().__init__(id, make, model, color, year, price)
        self.airSuspension = airSuspension

    def setairSuspension(self, airSuspension):
        self.airSuspension = airSuspension

    def getairSuspension(self):
        return self.airSuspension

    def calculatePriceWithTax(self):
        return super().getPrice() * 1.87

    def __str__(self) -> str:
        return super().__str__() + "airSuspension : {airSuspension}".format(airSuspension=self.airSuspension)

