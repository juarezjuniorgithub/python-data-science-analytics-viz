class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

student_one = Student("Juarez", 1)
print("Size of student class object:", student_one.__sizeof__())

list_one = [1, 2, 3, 4, 5]
tuple_one = (1, 2, 3, 4, 5)
dictionary_one = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5}

print("Size of list: ", list_one.__sizeof__())
print("Size of tuple: ", tuple_one.__sizeof__())
print("Size of dictionary: ", dictionary_one.__sizeof__())