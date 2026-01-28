# Създай обектно-ориентирана система за управление на автомобили, отдавани под наем. Проектирай кода с ясна структура, използвайки класове, наследяване и капсулация. Базовият клас Car трябва да включва следните свойства: id, brand, model, year, base_price_per_day, mileage, fuel_type, license_category и is_available. Класът трябва да съдържа методи за изчисляване на цената за наемане, промяна на статуса като наличен или неналичен и представяне на информация за автомобила. Създай следните подкласове на Car с модификатори върху базовата цена: икономичен автомобил с 10% отстъпка, премиум автомобил с 10% надценка, SUV с 30% надценка и електрически автомобил с 20% отстъпка. Класът Customer трябва да съдържа име, телефон, имейл, категория на шофьорска книжка и списък с резервации. Той трябва да има методи за проверка дали клиентът може да наеме конкретен автомобил и за добавяне на резервации. Класът Reservation трябва да включва автомобил, клиент, крайна цена и статус (Pending, Active, Completed, Canceled), както и методи за активиране, приключване и отказ на резервацията. Класът CarRental трябва да управлява списък с автомобили, клиенти и резервации. Той трябва да предоставя методи за управление на автомобилите (добавяне, премахване, показване на налични автомобили, търсене по марка и модел, филтриране по тип гориво), методи за управление на клиенти (добавяне и търсене по телефонен номер), както и методи за управление на резервации (създаване с проверка за валидност, активиране, приключване, отказ и извеждане на активни и приключени резервации).

# Разширена версия на кода със стрингово представяне на резервации и допълнителни примери

class Car:
    def __init__(self, idcar, brand, model, year, bprice, km, fuel, dl, status=True):
        self.idcar = idcar
        self.brand = brand
        self.model = model
        self.year = year
        self.bprice = bprice
        self.km = km
        self.fuel = fuel
        self.dl = dl
        self.status = status

    def AvailabilityStatus(self):
        print(f"The {self.brand} {self.model} с id:{self.idcar} е {'наличен' if self.status else 'неналичен'}")

    def mark_available(self):
        self.status = True

    def mark_unavailable(self):
        self.status = False

    def __str__(self):
        return f"ID: {self.idcar}, {self.brand} {self.model} ({self.year}), Цена: {self.bprice}, Пробег: {self.km}, Гориво: {self.fuel}, Категория: {self.dl}, Статус: {'наличен' if self.status else 'неналичен'}"


class EconomyCar(Car):
    def __str__(self):
        return f"{self.brand} {self.model} (Economy) - Цена с отстъпка: {self.bprice * 0.9}"


class PremiumCar(Car):
    def __str__(self):
        return f"{self.brand} {self.model} (Premium) - Цена с надценка: {self.bprice * 1.1}"


class SUV(Car):
    def __str__(self):
        return f"{self.brand} {self.model} (SUV) - Цена с надценка: {self.bprice * 1.3}"


class ECar(Car):
    def __str__(self):
        return f"{self.brand} {self.model} (Electric) - Цена с отстъпка: {self.bprice * 0.8}"


class Customer:
    def __init__(self, name, phone, email, dlcategory):
        self.name = name
        self.phone = phone
        self.email = email
        self.dlcategory = dlcategory
        self.reservations = []

    def RentCheck(self, car: Car):
        if self.dlcategory == car.dl:
            print(f"[RentCheck] {self.name}: Валидна шофьорска книжка за {car.brand} {car.model}")
            return True
        else:
            print(f"[RentCheck] {self.name}: Невалидна шофьорска книжка за {car.brand} {car.model}")
            return False

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def __str__(self):
        return f"{self.name}, {self.email}, Тел: {self.phone}, Категория: {self.dlcategory}"


class Reservation:
    def __init__(self, car: Car, customer: Customer):
        self.car = car
        self.customer = customer
        self.final_price = car.bprice
        self.status = "Pending"

    def activate(self):
        if self.car.status:
            self.status = "Active"
            self.car.mark_unavailable()
            print(f"[Reservation] Активирана резервация: {self.customer.name} -> {self.car.brand} {self.car.model}")
        else:
            print("[Reservation] Колата не е налична!")

    def complete(self):
        self.status = "Completed"
        self.car.mark_available()
        print(f"[Reservation] Резервацията е приключена: {self.customer.name} -> {self.car.brand} {self.car.model}")

    def cancel(self):
        self.status = "Canceled"
        self.car.mark_available()
        print(f"[Reservation] Резервацията е отказана: {self.customer.name} -> {self.car.brand} {self.car.model}")

    def __str__(self):
        return f"Резервация({self.status}) - {self.customer.name} | {self.car.brand} {self.car.model} | Цена: {self.final_price}"


class CarRental:
    def __init__(self, cars=None, customers=None, reservations=None):
        # Приема None или списъци; ако са None — инициира празни списъци
        self.cars = cars if cars is not None else []
        self.customers = customers if customers is not None else []
        self.reservations = reservations if reservations is not None else []

    def add_car(self, car: Car):
        self.cars.append(car)

    def remove_car(self, car_id):
        self.cars = [i for i in self.cars if i.idcar != car_id]

    def show_available_cars(self):
        return [str(i) for i in self.cars if i.status]

    def search_by_brand_model(self, brand, model):
        return [str(i) for i in self.cars if i.brand == brand and i.model == model]

    def filter_by_fuel(self, fuel_type):
        return [str(i) for i in self.cars if i.fuel == fuel_type]

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def find_customer_by_phone(self, phone):
        for i in self.customers:
            if i.phone == phone:
                return i
        return None

    def create_reservation(self, car_id, customer: Customer):
        car = next((i for i in self.cars if i.idcar == car_id), None)
        if car and customer.RentCheck(car) and car.status:
            reservation = Reservation(car, customer)
            self.reservations.append(reservation)
            customer.add_reservation(reservation)
            print(f"[create_reservation] Успешна: {customer.name} -> {car.brand} {car.model}")
            return reservation
        else:
            print("[create_reservation] Резервацията е невалидна!")
            return None

    def get_active_reservations(self):
        return [str(i) for i in self.reservations if i.status == "Active"]

    def get_completed_reservations(self):
        return [str(i) for i in self.reservations if i.status == "Completed"]


# Създаване на множество обекти за демонстрация
car1 = EconomyCar(1, "Toyota", "Yaris", 2018, 50, 120000, "Petrol", "B", True)
car2 = PremiumCar(2, "BMW", "5 Series", 2020, 120, 80000, "Diesel", "B", True)
car3 = SUV(3, "Audi", "Q7", 2021, 150, 60000, "Diesel", "B", True)
car4 = ECar(4, "Tesla", "Model 3", 2022, 100, 30000, "Electric", "B", True)

# Допълнителни коли
car5 = EconomyCar(5, "Hyundai", "i20", 2019, 40, 90000, "Petrol", "B", True)
car6 = SUV(6, "Volvo", "XC90", 2019, 140, 70000, "Diesel", "B", True)
car7 = ECar(7, "Nissan", "Leaf", 2020, 80, 40000, "Electric", "B", False)  # в момента не е налична

# Клиенти
customer1 = Customer("Иван Петров", "0888123456", "ivan@example.com", "B")
customer2 = Customer("Мария Георгиева", "0899123456", "maria@example.com", "B")
customer3 = Customer("Георги Стоянов", "0877123456", "georgi@example.com", "B")

# Инициализация на системата с предварително добавени списъци (пример)
rental_system = CarRental(cars=[car1, car2], customers=[customer1], reservations=[])

# Добавяме още коли и клиенти чрез методите на системата
rental_system.add_car(car3)
rental_system.add_car(car4)
rental_system.add_car(car5)
rental_system.add_car(car6)
rental_system.add_car(car7)

rental_system.add_customer(customer2)
rental_system.add_customer(customer3)

# Демонстрации: създаване + активиране на резервации
reservation1 = rental_system.create_reservation(1, customer1)  # Toyota Yaris
if reservation1:
    reservation1.activate()

reservation2 = rental_system.create_reservation(4, customer2)  # Tesla Model 3
if reservation2:
    reservation2.activate()

# Опит за резервация на не-налична кола (car7)
reservation3 = rental_system.create_reservation(7, customer3)  # Nissan Leaf (status=False)
if reservation3:
    reservation3.activate()

# Премахваме кола от автопарка (пример)
rental_system.remove_car(5)  # премахваме Hyundai i20

# Приключваме първата резервация и анулираме втората (пример)
if reservation1:
    reservation1.complete()

if reservation2:
    reservation2.cancel()

# Проверки и изходи
print("\nНалични коли:")
for c in rental_system.show_available_cars():
    print(c)

print("\nТърсене BMW 5 Series:")
for c in rental_system.search_by_brand_model("BMW", "5 Series"):
    print(c)

print("\nФилтриране по Diesel:")
for c in rental_system.filter_by_fuel("Diesel"):
    print(c)

print("\nАктивни резервации:")
for r in rental_system.get_active_reservations():
    print(r)

print("\nПриключени резервации:")
for r in rental_system.get_completed_reservations():
    print(r)

print("\nРезервации на клиентите:")
for cust in rental_system.customers:
    print(f"{cust.name} има {len(cust.reservations)} резервации:")
    for r in cust.reservations:
        print("  -", r)
