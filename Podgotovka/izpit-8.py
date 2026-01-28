# Zad 2
class Employee:
    def __init__(self, i_num, fname, lname, work_experience, education_level, salary, age):
        self.i_num = i_num
        self.fname = fname
        self.lname = lname
        self.work_experience = work_experience
        self.education_level = education_level
        self.salary = salary
        self.age = age

    def display_info(self):
        print(f"i_num:{self.i_num}\nfname:{self.fname}\nlname:{self.lname}\nwork_exp:{self.work_experience}\nedu_level:{self.education_level}\nsalary:{self.salary}\nage:{self.age}")

    def bonus(self):
        bonus = 0
        if self.education_level.lower() == "висше образование".lower():
            bonus = self.salary*0.05
        elif self.education_level.lower() == "средно образование".lower():
            bonus = self.salary*0.02
        elif self.education_level.lower() == "основно образование".lower():
            bonus = 0
        bonus += self.salary*self.work_experience*0.012
        return bonus


employee_list = []
n = int(input("Брой служители:"))
for i in range(n):
    print(f"\nСлужител номер {i+1}")
    i_num = int(input("i_num:"))
    fname = input("fname:")
    lname = input("lname:")
    work_experience = int(input("work_exp:"))
    education_level = input("edu_lvl:")
    salary = float(input("salary:"))
    age = int(input("age:"))

    employee_list.append(Employee(i_num, fname, lname,
                         work_experience, education_level, salary, age))


def sort_employee(employees):
    employees.sort(key=lambda x: x.age, reverse=True)
    for e in employees:
        e.display_info()


def search_by_name(employees):
    found = False
    name_f = input("Търсено първо име:")
    name_l = input("Търсена фамилия:")
    for e in employees:
        if e.fname.lower() == name_f.lower() and e.lname.lower() == name_l.lower():
            e.display_info()
            found = True
    if not found:
        print("Not found!!!")


def print_by_education_experience(employees):
    found = False
    edu = input("Търсено образование:")
    exp = int(input("Търсен стаж"))
    for e in employees:
        if e.education_level.lower() == edu.lower() and e.work_experience == exp:
            e.display_info()
            found = True
    if not found:
        print("Not found!!!")


def remove_employee(employees):
    found = False
    num = int(input("Търсен служебен номер:"))
    for e in employees:
        if e.i_num == num:
            employees.remove(e)
            print("Information deleted!!!")
            found = True
            break
    if not found:
        print("Wrong i_num!!!")
