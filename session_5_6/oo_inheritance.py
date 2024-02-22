# superclass (parent)
class Animal:

    def eat(self):
        print( "I can eat!")
    
    def sleep(self):
        print("I can sleep!")

# subclass (child)
class Dog(Animal):
    
    def bark(self):
        print("I can bark! Woof woof!!")

# subclass (child)
class Cat(Animal):
    
    def meow(self):
        print("I can meow!")

# Create object of the Dog class
dog1 = Dog()

# Calling members of the superclass
dog1.eat()
dog1.sleep()

# Calling member of the subclass
dog1.bark();

cat1 = Cat()
cat1.eat()
cat1.sleep()
cat1.meow()
