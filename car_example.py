import car

dd_car = car.Car('white')
dd_car.report()
print(dd_car)

print(dd_car.color)

dd_car.set_color('pink')
dd_car.set_cylinders(10)

print(dd_car)

print(dd_car.get_cylinders())