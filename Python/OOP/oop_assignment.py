#Assignment 1: Design your own class!
class Favorites:
    def __init__(self, phone, car):
        self.phone = phone
        self.car = car

    def drive(self):
        print(f'I used {self.phone} while driving {self.car}')

class Dearest(Favorites):
        def drive(self):
            print(f'My dearest choice is driving a {self.car} with my {self.phone}')

fav = Favorites('Nokia', 'Benz')
fav.drive()

dear = Dearest('JEEP', 'Motorolla')
dear.drive()

#Activity 2: Polymorphism Challenge!
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print('Driving')

class Plane(Vehicle):
    def move(self):
        print('Flying')

class Boat(Vehicle):
    def move(self):
        print('Sailing')

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
