import enum 

class CarSize(enum.Enum): 
    small = "s"
    medium = "m"
    large = "l"

class Car:
    def __init__(self, size, id):
        if size == "s" :
            self.carSize = CarSize.small
        elif size == "m" :
            self.carSize = CarSize.medium
        elif size == "l":
            self.carSize = CarSize.large
        self.car_id = id

class Store :
    def __init__(self) :
        self.parked_cars = {}
        
    def additem(self, id, size):
        self.parked_cars[str(id)] = size

    def delitem(self, id):
        del self.parked_cars[str(id)]

    def isAvailable(self, id):
        if str(id) in self.parked_cars:
            return True
        else:
            return False
            
class ParkingGarage:
    small_spots = 0
    medium_spots = 0
    large_spots = 0

    def __init__(self, s, m, l) :
        self.small_spots = s
        self.medium_spots = m
        self.large_spots = l
        self.store_obj = Store()
        
    def park(self, car):
        if self.isSpotAvailable(car.carSize) :
            available_spot = self.parkCar(car)
            self.removeSpot(available_spot)
            self.store_obj.additem(car.car_id, car.carSize)
            print ('Parked '+car.car_id)
        else :
            print ('Failed to park '+car.car_id)
            
    def retreive(self, id):
        if self.store_obj.isAvailable(id) :
            carSize = self.store_obj.parked_cars.get(str(id))
            self.addSpot(carSize)
            self.store_obj.delitem(id)
            print ('Retreived '+id)
        else :
            print('Failed to retreive '+id)
            
    def parkCar(self, car) :
        available_spot = CarSize.small
        
        if self.small_spots > 0 and car.carSize == CarSize.small:
            available_spot = CarSize.small
        elif self.medium_spots > 0 and (car.carSize == CarSize.small or car.carSize == CarSize.medium):
            available_spot = CarSize.medium
        elif self.large_spots > 0 and (car.carSize == CarSize.large or car.carSize == CarSize.small):
            available_spot = CarSize.large
            
        return available_spot
        
    def isSpotAvailable(self, carSize) :
        if carSize == CarSize.small :
            if (self.small_spots+self.medium_spots+self.large_spots) > 0:
                return True
            else :
                return False
        elif carSize == CarSize.medium :
            if (self.medium_spots+self.large_spots) > 0:
                return True
            else :
                return False
        elif carSize == CarSize.large :
            if self.large_spots > 0 :
                return True
            else :
                return False
                
        return False
    
    def addSpot(self, size) :
        if size == CarSize.small :
            self.small_spots = self.small_spots + 1
        elif size == CarSize.medium :
            self.medium_spots = self.medium_spots + 1
        elif size == CarSize.large :
            self.large_spots = self.large_spots + 1
    
    def removeSpot(self, size) :
        if size == CarSize.small :
            self.small_spots = self.small_spots - 1
        elif size == CarSize.medium :
            self.medium_spots = self.medium_spots - 1
        elif size == CarSize.large :
            self.large_spots = self.large_spots - 1
    
def main():
    s = 4
    m = 5
    l = 1
    operations = ["Park l 101", "Park l 102", "Retreive 101", "Park l 103", "Retreive 101"]
    parking_garge = ParkingGarage(s, m, l)
    for operation in operations :
        oper = operation.split()
        mode = oper[0]
        if mode.lower() == "park" :
            car_obj = Car(oper[1], oper[2])
            parking_garge.park(car_obj)
        elif mode.lower() == "retreive" :
            parking_garge.retreive(oper[1])
if __name__== "__main__":
  main()
