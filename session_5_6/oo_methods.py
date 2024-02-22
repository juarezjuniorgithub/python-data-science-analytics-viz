class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def hello(self):
    print("Hello my name is " + self.name)

person_object = Person("James", 33)
person_object.hello()