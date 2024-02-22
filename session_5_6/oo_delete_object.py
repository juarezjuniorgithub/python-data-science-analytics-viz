class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

first_person = Person("Patrick", 22)
print(first_person.name)
print(first_person.age)

second_person = Person("Thomas", 35)
print(second_person.name)
print(second_person.age)

third_person = Person("Peter", 50)
print(third_person)

del third_person