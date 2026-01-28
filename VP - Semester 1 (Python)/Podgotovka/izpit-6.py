# izpit 6 - zad.1


while True:
    try:
        n = int(input("n(15<n<35):"))
        if 15 < n < 35:
            break
        else:
            print("n trqbva da otgovarq na 15<n<35")
            continue
    except ValueError:
        print("Nevaliden vhod")

list1 = []
for i in range(n):
    while True:
        try:
            num = int(input(f"Chislo {i+1}:"))
            if 30 < num < 3000:
                list1.append(num)
                break
            else:
                print("num trqbva da otgovarq na 30<num<3000")
        except ValueError:
            print("Nevaliden vhod")

print(f"List1:{list1}")

count_el = 0
for x in list1:
    stot = (x//100) % 10
    if stot % 4 == 0:
        count_el += 1
if count_el > 0:
    print(f"count_el:{count_el}")

min_index = None
min_value = None
for i in range(len(list1)):
    if list1[i] % 6 == 4:
        if min_value is None or list1[i] < min_value:
            min_value = list1[i]
            min_index = i
if min_value is not None:
    print(f"min_value:{min_value}\nmin_index:{min_index}")

list2 = [x for x in list1 if 9 < x < 100 and (x % 2 == 0 or x % 3 == 0)]
print(f"List2:{list2}")

count_avg = 0
sum_avg = 0
for i in range(len(list2)):
    if i % 2 != 0:
        count_avg += 1
        sum_avg += list2[i]
if count_avg > 0:
    print(f"Avg:{round((sum_avg/count_avg),2)}")

min_even = None
for x in list2:
    if x % 2 == 0:
        if min_even is None or x < min_even:
            min_even = x
if min_even is not None:
    list2.remove(min_even)

max_odd = None
min_odd = None
for x in list2:
    if x % 2 != 0:
        if min_odd is None or x < min_odd:
            min_odd = x
        if max_odd is None or x > max_odd:
            max_odd = x
prod = min_odd*max_odd
print(f"prod:{prod}")
list2.insert(0, prod)
print(f"List2:{list2}")

# izpit 6 - zad.2


class Worker:
    def __init__(self, worker_num, fname, lname, work_experience_company, total_year_experience, salary, age):
        self.worker_num = worker_num
        self.fname = fname
        self.lname = lname
        self.work_experience_company = work_experience_company
        self.total_year_experience = total_year_experience
        self.salary = salary
        self.age = age

    def worker_information(self):
        print(f"worker_num:{self.worker_num}\nfname:{self.fname}\nlname:{self.lname}\nwork_experience_company:{self.work_experience_company}\ntotal_years_experience:{self.total_year_experience}\nsalary:{self.salary}\nage:{self.age}")

    def salary_bonus(self):
        if 5 <= self.work_experience_company <= 10:
            bonus = self.salary*0.015
        elif self.work_experience_company > 10:
            bonus = self.salary*0.02
        else:
            bonus = self.salary*0.005
        return bonus


workers_list = []

while True:
    try:
        n = int(input("Broi rabotnici:"))
        break
    except ValueError:
        print("Nevaliden vhod")
        continue

for i in range(n):
    while True:
        try:
            print(f"\nRabotnik {i+1}")
            worker_num = int(input("worker_num:"))
            fname = input("fname:")
            lname = input("lname:")
            work_experience_company = int(input("work_experience_company:"))
            total_year_experience = int(input("total_years_experience:"))
            salary = int(input("salary:"))
            age = int(input("age:"))
            workers_list.append(Worker(
                worker_num, fname, lname, work_experience_company, total_year_experience, salary, age))
            break
        except ValueError:
            print("Nevaliden vhod")
            continue


def search_by_num(workers, number):
    for w in workers:
        if w.worker_num == number:
            return True
    return False


def search_by_name_experience(workers, name, experience):
    found = False
    for w in workers:
        if w.fname.lower() == name.lower() and w.work_experience_company == experience:
            found = True
            w.worker_information()
    if not found:
        print("Nevalidno ime i staj vuv firmata")


def avg_worker_age(workers):
    count_w = 0
    sum_age = 0
    for w in workers:
        if w.work_experience_company > 10:
            count_w += 1
            sum_age += w.age
    if count_w > 0:
        return round((sum_age/count_w), 2)


def remove_worker(workers, num):
    for w in workers:
        if w.worker_num == num:
            workers.remove(w)
            return "information deleted!!!"
    return "Wrong worker num!!!"
