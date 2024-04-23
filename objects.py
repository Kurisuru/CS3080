class Car:
    
    wheels = 4
    
    #color = 'blue'
    
    def set_color(self, color):
        
        self.color = color
        
    def report(self):
        print("The car's color is", self.color)
        print("The car has", Car.wheels, "wheels")
        print()
        
    def __init__(self, color = 'black'):
        
        self.color = color
    
moms_car = Car('green')
moms_car.report()

moms_car.set_color('red')
moms_car.report()

dads_car = Car()
dads_car.report()
