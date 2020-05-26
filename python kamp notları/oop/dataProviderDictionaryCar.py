from oop.car import Car


class DataProviderDictionaryCar:
    carList = None

    def __init__(self) -> None:
        global carList
        carList = dict()

    def insert(self, car):
        global carList
        carList[car.getId()] = car

    def update(self, car):
        global carList
        for carId, carInfo in carList.items():
            if carId == car.getId():
                carList[carId] = car
                return True
        return False

    def delete(self, id):
        global carList
        for carId, carInfo in carList.items():
            if carId == id:
                del carList[carId]
                return True
        return False

    def getList(self):
        global carList
        return carList

    def getById(self, id):
        global carList
        for carId, carInfo in carList.items():
            if carId == id:
                return carInfo
            return False

