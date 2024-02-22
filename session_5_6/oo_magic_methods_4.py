# magic methods 
class Sample:
    def __new__(self, parameter):
        print("New invoked", parameter)
        return super().__new__(self)
    
    def __init__(self, parameter):
        print("Init invoked", parameter)

obj = Sample("a")
obj2 = Sample("b")

print(obj.__sizeof__())
print(dir(obj))

print(obj2.__sizeof__())
print(dir(obj2))