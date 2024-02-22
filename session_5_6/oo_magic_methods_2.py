class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def __str__(self):
        return("{} {}".format(self.name, self.roll_no))
    
student_one = Student("Juarez", 1)
student_two = Student("David", 2)

print(student_one)
print(student_two)

print(type(student_one))
print(type(student_two))

print(dir(student_one))
#print(dir(student_two))