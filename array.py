cars = ["Ford", "Volvo", "BMW"]

""" #Get the value of index 
print(cars[0])

#Modify the value of the first array item:
cars[2] = "toyota"
print(cars)

#The Length of an Array
print(len(cars))

#Looping Array Elements
for index,item in enumerate(cars) : print(index, item)

#Adding Array Elements
cars.append("Honda")
print(cars)

#Removing Array Elements Wirh Index
cars.pop(1)
print(cars)

#Removing Array Elements Wirh Value
cars.remove('Honda')
print(cars) """

""" Method Array """
# clear =  cars.clear()
# print(cars)

cars_1 = cars.copy()
cars_1.append("Honda")
cars_1.sort()
cars_1.reverse()

print(cars_1)
