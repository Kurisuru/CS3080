class Car:
    
    wheels = 4
    
    #color = 'blue'
    
    def set_color(self, color):
        
        self.color = color
        
    def report(self):
        print("The car's color is", self.color)
        print("The car has", Car.wheels, "wheels")
        print()
        
    def __init__(self, color = 'black', cylinders=6):
        
        self.color = color
        self.__engine = cylinders
        
    def __str__(self):
        s = 'VEHICLE REPORT\n'
        s += "COLOR: %s\n" % (self.color)
        s += "WHEELS: %d\n" % (Car.wheels)
        s += "CYLINDERS: %d\n" % (self.get_cylinders())
        s += "\n"
        return s
    def get_cylinders(self):
        
        return self.__engine
    
    def set_cylinders(self, cylinders):
        
        self.__engine = cylinders
        
def f(a, b, c, d, e):
    a.append('Harry')
    a = ['Harry']
    a.append('Alice')
    b =  b[1]
    c['Harry'] = 44
    d += 'abcd'
    e += 10
    pass

x = ['Tom', 'Sue', 'Bob']
y = ('Tom', 'Sue', 'Bob')
z = {'Tom':41, 'Sue':42, 'Bob':43}
s = 'ABCD'
n = 42

f(x, y, z, s, n)


print(x)
print(y)
print(z)
print(s)
print(n)


h = ([1,2],(1,2))
j = {}


print(j)
        
'''        
if __name__ == '__main__':
    moms_car = Car('green')
    moms_car.report()
    
    moms_car.set_color('red')
    moms_car.report()

    dads_car = Car()
    dads_car.report()
'''