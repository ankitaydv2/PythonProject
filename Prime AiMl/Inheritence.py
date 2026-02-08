class Employee:
    start_time = "10am"
    end_time = "2pm"

    def change_time(self, new_end_time):
        self.end_time = new_end_time

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

class AdminStaff(Employee):
    def __init__(self , role):
        self.role = role

class Account(AdminStaff):
    def __init__(self, number, role):
        super().__init__(role)
        self.number = number

t1 = Teacher("Math")
t1.change_time("5pm")

acc1 = Account(2028 , "Head")

staff1 = AdminStaff("Manager")

print(acc1.role, acc1.number, acc1.start_time, acc1.end_time)
#print(staff1.role, staff1.start_time, staff1.end_time)
#print(t1.subject, t1.start_time, t1.end_time)


#MULTIPLE INHERITENCE

class Head:
    def __init__(self, salary):
        self.salary = salary

class HR:
    def __init__(self, post):
        self.post = post

class TPO(Head, HR):
    def __init__(self, salary, post, placed):
        super().__init__(salary)
        HR.__init__(self, post)
        self.placed = placed

tpo1 = TPO(25_000, "High" , "yes")
print(tpo1.placed, tpo1.post, tpo1.salary)