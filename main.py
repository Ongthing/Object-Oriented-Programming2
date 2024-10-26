from car import Car
car_1 = Car("ongthing","OTL",2012,"yello")
car_2 = Car("ford","mostag",2013,"red")
car_1.wheels = 2
print(car_1.wheels)
print(car_2.wheels)
#or
# from car import Car
# print(Car.wheels)
#or
from car import Car
car_1 = Car("ongthing","OTL",2012,"yello")
car_2 = Car("ford","mostag",2013,"red")
Car.wheels = 2
print(car_1.wheels)
print(car_2.wheels) #same