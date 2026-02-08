# class Employee:
#     def get_designation(self):
#         print("Designation = Employee")
#
# class Teacher(Employee):
#     def get_designation(self):
#         print("designation = Teacher")
#
# t1 = Teacher()
# t1.get_designation()


class Teacher():
    def get_designation(self):
        print("Designation = Teacher")

class Accountant():
    def get_designation(self):
        print("Designation = Accountant")

t1 = Teacher()
t1.get_designation()

acc1 = Accountant()
acc1.get_designation()