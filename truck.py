import car

class Truck(car.Car):

    def __init__(self, drive):
        car.Car.__init__(self, color='black', cylinders=8)
        self.drive = drive
        
    def __str__(self):
        
        s = 'VEHICLE REPORT\n'
        s += "COLOR: %s\n" % (self.color)
        s += "WHEELS: %d\n" % (Car.wheels)
        s += "CYLINDERS: %d\n" % (self.get_cylinders())
        s += "DRIVE: %dx%d\n" % (Truck.wheels, self.drive)
        s += "\n"
        
        return s
    
    
    
my_truck = Truck(4)
print(my_truck)