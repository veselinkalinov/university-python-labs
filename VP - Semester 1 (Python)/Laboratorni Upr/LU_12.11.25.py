# Задача 1:

class Person:
    def __init__(self, name, family, age, nationality, phnum):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality
        self.phnum = phnum

    def print(self):
        print(
            f"Name: {self.name} {self.family}, Age: {self.age}, Nationality: {self.nationality}, Phone Number: {self.phnum}")


class Student(Person):
    def __init__(self, name, family, age, phnum, university, year_of_edu, nationality):
        super().__init__(name, family, age, nationality, phnum)
        self.university = university
        self.year_of_edu = year_of_edu

    def print(self):
        print(f"Name: {self.name} {self.family}, Age: {self.age}, Nationality: {self.nationality}, Phone Number:{self.phnum}; "
              f"University: {self.university}, Year of education: {self.year_of_edu}")


student1 = Student("Ivan", "Ivanov", 18, 359884552153,
                   "TU - Sofia", 3, "Bulgarian")
student1.print()


class Lecturer(Person):
    def __init__(self, name, family, age, nationality, phnum, university, experience):
        super().__init__(name, family, age, nationality, phnum)
        self.university = university
        self.experience = experience

    def print(self):
        print(f"Name: {self.name} {self.family}, Phone Number: {self.phnum}, Age: {self.age}, Nationality: {self.nationality}, University: {self.university}, Experience: {self.experience}")


lecturer1 = Lecturer("Ivan", "Ivanov", 42, "Bulgarian",
                     359887645324, "TU - Sofia", 12)
lecturer1.print()

# Задача 2:


class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def print(self):
        print(f'Brand: {self.brand}, Speed: {self.speed}')


class Car(Vehicle):
    def __init__(self, brand, speed):
        super().__init__(brand, speed)

    def move(self):
        print(f"The {self.brand} is moving with {self.speed} km/h")


class Bike(Vehicle):
    def move(self):
        print(f"The {self.brand} is moving with {self.speed} km/h")


vehicle1 = Vehicle("Opel", 110)

car1 = Car("Opel", 110)
car1.move()

bike1 = Bike("Honda", 200)
bike1.move()

# Зад 3: Създайте клас BankAccount, с owner и balance. Да се добавят методи които могат да добавят към баланса и да изваждат от него ако има достатъчно пари, също така и метод трансфер към друг акаунт, който да трансферира от един акаунт в друг. Създайте обекти и използвайте трите метода.


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}: Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(
                f"{self.owner}: Withdrawal of {amount} failed — insufficient funds (balance {self.balance}).")
            return False
        self.balance -= amount
        print(f"{self.owner}: Withdrew {amount}. New balance is {self.balance}.")
        return True

    def transfer(self, transfer_account, amount):
        if self.withdraw(amount):
            transfer_account.deposit(amount)
            print(
                f"Transferred {amount} from {self.owner} to {transfer_account.owner}.")
            return True
        print(
            f"Transfer of {amount} from {self.owner} to {transfer_account.owner} failed.")
        return False


account1 = BankAccount("Ivan Ivanov", 1000)
account2 = BankAccount("Petar Petrov", 2000)

account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)
account1.transfer(account2, 300)
account1.transfer(account2, 2000)

account2.deposit(1000)
account2.withdraw(500)
account2.transfer(account1, 700)
account2.transfer(account1, 3000)
