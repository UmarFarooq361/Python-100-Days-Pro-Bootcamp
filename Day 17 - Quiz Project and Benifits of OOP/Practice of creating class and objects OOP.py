class Car:
    def __init__(self, seats):
        self.seats = seats
        print(f"creating object of the car classand it has {seats} seats")
    def enter_race(self , seats):
        self.seats = seats
        print(f"In race mode car has {seats} seats")


carolla = Car(6)
print(carolla.enter_race(2))

