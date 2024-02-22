vehicles = ["Ford", "Cupra", "BMW", "Honda", "Daimler", "Mazda"]
vehicles.append("Fiat")
print(vehicles)

trucks = ["Volvo", "Iveco"]
vehicles.append(trucks)
print(vehicles)

trucks.clear()
print(trucks)

print(vehicles)

fruits = ["orange", "apples"]
copy_of_fruits = fruits.copy()
print(fruits)
print(copy_of_fruits)

fruits.clear()
print(fruits)
print(copy_of_fruits)

fruits = ['apple', 'banana', 'cherry']
counter = fruits.count("cherry")
# counter = 1


print(str(counter))

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
