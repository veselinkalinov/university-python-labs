
'''1зад. Напишете програма, в която е описан клас. Обектите на класа трябва да имат поле, представляващо числов списък. Този списък се формира на основата на списък, предаден като аргумент на конструктора. При това от списъка аргумент в списъка поле се включват само числовите елементи(елементите от други типове се игнорират). Също така трябва да се дефинират два метода:
Първият метод показва съдържанието на полето списък, а вторият метод изчислява средната стойност на елементите на полето списък.'''


import math


class NumberList:
    def __init__(self, input_list):

        self.input_list = input_list
        self.numbers = []
        for el in self.input_list:
            if type(el) in (int, float):
                self.numbers.append(el)

    def show_content(self):
        print(f"Списък с числа: {self.numbers}")

    def calculate_average(self):
        if not self.numbers:
            return 0

        total_sum = sum(self.numbers)
        count = len(self.numbers)
        return total_sum / count


raw_data = [10, "текст", 5.5, [1, 2], 20, True, 4.5]

my_object = NumberList(raw_data)

my_object.show_content()

average_val = my_object.calculate_average()
print(f"Средна стойност: {average_val}")

'''2зад. Напишете програма, в която е описан клас и функция,
предназначена за създаване на списък от обекти. Обектите на класа трябва да имат поле(предназначено за записване на целочислена стойност). При извикване на функцията се предава като аргумент цяло число, определящо броя на обектите в списъка. Полетата на обектите се запълват с цели нечетни числа.'''


class NumberContainer:
    def __init__(self, value):
        self.value = value

    def __repr__(self):

        return f"Obj({self.value})"


def create_odd_list(n):

    objects_list = []
    current_odd_number = 1

    for _ in range(n):

        new_obj = NumberContainer(current_odd_number)

        objects_list.append(new_obj)

        current_odd_number += 2

    return objects_list


count = 5
my_list = create_odd_list(count)

print(f"Списък от {count} обекта с нечетни числа:")
print(my_list)

for obj in my_list:
    print(f"Стойност в полето на обекта: {obj.value}")


'''Ззад. Напишете програма, в която е описана функция. На функцията се предават като аргументи два обекта от един и същи клас. Всеки обект има поле представляващо списък от цели числа. Функцията връща като резултат обект от същия клас. Полето списък на този обект се получава посредством сумирането на съответните елементи от полетата списъци на обектите, предадени като агументи на функцията. Ако в тези обекти списъците са с различна дължина, то списъка резултат е с размера на по-големият от двата списъка, като недостигащите елементи в списъка резултат се запълват с нули.'''


class IntegerList:
    def __init__(self, numbers):
        self.data = numbers

    def show(self):
        print(f"Списък: {self.data}")


def sum_list_objects(obj1, obj2):

    list1 = obj1.data
    list2 = obj2.data

    len1 = len(list1)
    len2 = len(list2)
    max_len = max(len1, len2)

    result_list = []

    for i in range(max_len):

        val1 = list1[i] if i < len1 else 0

        val2 = list2[i] if i < len2 else 0

        total = val1 + val2
        result_list.append(total)

    return IntegerList(result_list)


o1 = IntegerList([10, 20, 30])

o2 = IntegerList([1, 2, 3, 4, 5])

print("Обект 1:")
o1.show()
print("Обект 2:")
o2.show()

print("-" * 20)

result_obj = sum_list_objects(o1, o2)

print("Резултатен обект (сума):")
result_obj.show()


'''4зад. Дефинирайте клас Shape с едно поле задаващо вида на фигурата. Дефинирайте клас Square и клас Circle, които наследяват Shape.
Класът Square и класът Circle имат предефинирана функция_init__ която приема дължина(радиус) като аргумент.
И трите класа имат метод за намиране на лице, като лицето на Shape е 0 по подразбиране. Потребителя въвежда вида на фигурата и на тази база се създава обект от съответния клас. След това се извиква метода за намиране на лице за съответния обект. Добавете обработка на изключения.'''


class Shape:
    def __init__(self, kind):
        self.kind = kind

    def get_area(self):
        return 0


class Square(Shape):
    def __init__(self, side):
        super().__init__("Квадрат")
        self.side = side

    def get_area(self):
        return self.side**2


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Кръг")
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    print("Моля, изберете вид фигура: square или circle")
    choice = input("Вашият избор: ").lower().strip()

    shape_object = None

    try:
        if choice == "square":
            side_input = input("Въведете дължина на страната: ")
            side = float(side_input)

            if side < 0:
                raise ValueError("Дължината не може да е отрицателна.")

            shape_object = Square(side)

        elif choice == "circle":
            radius_input = input("Въведете радиус: ")
            radius = float(radius_input)

            if radius < 0:
                raise ValueError("Радиусът не може да е отрицателен.")

            shape_object = Circle(radius)

        else:
            print("Неразпозната фигура.")

        area = shape_object.get_area()
        print(f"Фигура: {shape_object.kind}")
        print(f"Лице: {area:.2f}")

    except ValueError as e:
        print(f"ГРЕШКА: Невалидни данни! {e}")
    except Exception as e:
        print(f"Възникна неочаквана грешка: {e}")


'''5зад. Напишете програма, в която е дефиниран клас. В класа е описан конструктор, на който като аргумент се предават текст и цяло число в произволен порядък. Числото и текстът се присвояват като стойности на определени полета. Ако са предадени две текстови стойности, тогава се създава само текстово поле със стойност, получена от обединението на стойностите на аргументите. Ако като аргумент са предадени две числови стойности, тогава обектът ще има само поле с целочислена стойност, равна на сумата от стойностите на аргументите. В останалите случаи полета на обекта не се създават. Създайте на основата на класа обекти и проверете функционалността на кода.'''

'''бзад. Николай трябва да провери дали е възможно да се образува триъгълник от представените страни с условна дължина. За да направи това, той реши да създаде клас TriangleChecker, който приема само положителни числа. Методът is_triangle() връща следните стойности(в зависимост от ситуацията):
- Ура, можете да построите триъгълник!
- Нищо няма да работи с отрицателни числа!
- Трябва да въведете само числа!
- Жалко, но не можете да направите триъгълник от това!
Дефинирайте метод get_triangle_type(), който връща като резултат типа на триъгълника: равностранен, равнобедрен или разностранен'''


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        try:
            side_a = float(self.a)
            side_b = float(self.b)
            side_c = float(self.c)

        except (ValueError, TypeError):
            return "Трябва да въведете само числа!"

        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            return "Нищо няма да работи с отрицателни числа!"

        if (side_a + side_b > side_c) and \
           (side_a + side_c > side_b) and \
           (side_b + side_c > side_a):
            return "Ура, можете да построите триъгълник!"
        else:
            return "Жалко, но не можете да направите триъгълник от това!"

    def get_triangle_type(self):
        check_result = self.is_triangle()

        if check_result != "Ура, можете да построите триъгълник!":
            return check_result

        val_a = float(self.a)
        val_b = float(self.b)
        val_c = float(self.c)

        if val_a == val_b == val_c:
            return "Равностранен"
        elif val_a == val_b or val_a == val_c or val_b == val_c:
            return "Равнобедрен"
        else:
            return "Разностранен"


t1 = TriangleChecker("десет", 5, 5)
print(f"t1 - {t1.is_triangle()}")

t2 = TriangleChecker(10, -5, 10)
print(f"t2 - {t2.is_triangle()}")

t3 = TriangleChecker(1, 2, 10)
print(f"t3 - {t3.is_triangle()}")

t4 = TriangleChecker(5, 5, 8)
print(f"t4 - {t4.is_triangle()}")
print(f"Type: {t4.get_triangle_type()}")

t5 = TriangleChecker(5, 5, 5)
print(f"t5 - {t5.is_triangle()}")
print(f"Type: {t5.get_triangle_type()}")


'''7зад. Създайте клас Food с полета carbs, protein и fat, които се инициализират при създаването на обект от класа.
В класа е добавен метод calories(), който изчислява броят на калориите в обект от класа по следната схема: 4 калории за грам въглехидрати, 4 калории за всеки грам протеин и 9 калории за грам мазнини.
Създайте клас Recipe. Обектите от класа имат поле паме
(наименование на рецептата) и поле, представляващо списък с обекти от класа Food, наречен ingradients. Добавете метод в класа, наречен calories(), който връща общият брой на калориите за дадена рецепта. Добавете_str___ метод в класа Recipe, който връща името на рецептата. Създайте п на брой обекти от класа Recipe, като п се въвежда от потребителя и е цяло число по-голямо от 4 и по-малко от 15. За всяка една от рецептите отпечатайте името на рецептата и общият брой на калориите за тази рецепта.
Добавете обработка на изключения, там където е необходимо.'''


class Food:
    def __init__(self, carbs, protein, fat):
        if carbs < 0 or protein < 0 or fat < 0:
            raise ValueError(
                "Хранителните стойности не могат да бъдат отрицателни!")

        self.carbs = float(carbs)
        self.protein = float(protein)
        self.fat = float(fat)

    def calories(self):
        return (4 * self.carbs) + (4 * self.protein) + (9 * self.fat)


class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def calories(self):
        total_cals = 0
        for food_item in self.ingredients:
            total_cals += food_item.calories()
        return total_cals

    def __str__(self):
        return self.name


def generate_recipes(n):
    recipes_list = []

    egg = Food(1, 6, 5)
    flour = Food(76, 10, 1)
    sugar = Food(100, 0, 0)
    butter = Food(0, 0, 81)
    chicken = Food(0, 27, 4)
    rice = Food(28, 3, 0)

    for i in range(1, n + 1):

        if i % 2 == 0:
            rec_name = f"Солена гозба №{i}"

            ingr = [chicken, rice, butter]
        else:
            rec_name = f"Сладък десерт №{i}"

            ingr = [flour, sugar, egg, egg]

        new_recipe = Recipe(rec_name, ingr)
        recipes_list.append(new_recipe)

    return recipes_list

    while True:
        try:
            user_input = input("Въведете брой рецепти (между 4 и 15): ")
            n = int(user_input)

            if 4 < n < 15:
                break
            else:
                print(
                    "Грешка: Числото трябва да е строго по-голямо от 4 и по-малко от 15.")

        except ValueError:
            print("Грешка: Моля, въведете цяло число!")

    print(f"\n--- Генериране на {n} рецепти... ---")
    my_recipes = generate_recipes(n)

    print(f"{'ИМЕ НА РЕЦЕПТА':<20} | {'КАЛОРИИ':<10}")
    print("-" * 35)

    for recipe in my_recipes:
        print(f"{recipe}      | {recipe.calories():.2f} kcal")


'''8зад. Да се реализира система за управление на персонал в компания. За целта създайте клас Employee, който ще се наследява от различни видове служители като Мениджър и Програмист. Обектите на класа имат атрибутите: name(име на служителя), position(позиция в компанията), salary(заплата). В класа е дефиниран метод display_info(), който връща информация за служителя.
Създайте клас Manager и клас Developer, които наследяват класа Employee.
Клас Manager има допълнително поле department(отдел на мениджъра), както и методи: calculate_bonus() бонусът на мениджъра се изчислява като 10 % от основната заплата плюс 1000 лв. за ръководството на екип
display_info() - връща информация за мениджъра, включително отдела. Клас Developer има поле programming_languages(списък с програмни езици, които знае програмистът), както и методи: calculate_bonus() - бонусът на програмист се изчислява като 15 % от основната заплата плюс 200 лв. за всеки програмен език, който владее
display_info() - връща информация за програмиста, включително списъка с програмни езици. Създайте клас Company(компания) с атрибут employees(списък със служители) и методи: add_employee(employee) - метод за добавяне на служител в компанията, total_salary_expense() - метод за изчисляване на общите разходи за заплати на всички служители.display_all_employees() - метод за показване на информация за всички служители в компанията.'''

'''9зад. Създайте клас Phone със следните полета:
.
brand(марка) текстов низ
.
model(модел) текстов низ
.
price(цена)-дробно число
quantity(количество) цяло число
-
В класа трябва да бъде дефиниран метод display_info(), който принтира стойностите на всички полета на обекта.
Напишете функция create_phone_list(), която връща списък с обекти от
класа Рһопе
Напишете функция find_max_price_phone(phones), която намира и връща телефона с най-висока цена от списъка
Напишете функция calculate_average_price(phones), която изчислява и връща средноаритметичното от цените на всички телефони в списъка Напишете функция filter_by_brand(phones, brand), която връща списък само с телефоните от дадена марка. Марката се въвежда от клавиатурата'''


class Phone:
    def __init__(self, brand, model, price, quantity):
        self.brand = brand
        self.model = model
        self.price = float(price)
        self.quantity = int(quantity)

    def display_info(self):
        print(
            f"Марка: {self.brand} | Модел: {self.model} | Цена: {self.price:.2f} лв. | Наличност: {self.quantity}")


def create_phone_list():
    p1 = Phone("Samsung", "Galaxy S23", 1450.50, 10)
    p2 = Phone("Apple", "iPhone 14", 1800.00, 5)
    p3 = Phone("Xiaomi", "Redmi Note 12", 450.90, 20)
    p4 = Phone("Samsung", "Galaxy A54", 650.00, 15)
    p5 = Phone("Nokia", "3310 Reborn", 120.00, 50)

    return [p1, p2, p3, p4, p5]


def find_max_price_phone(phones):
    if not phones:
        return None

    max_phone = phones[0]

    for phone in phones:
        if phone.price > max_phone.price:
            max_phone = phone

    return max_phone


def calculate_average_price(phones):
    if not phones:
        return 0.0

    total_sum = 0
    for phone in phones:
        total_sum += phone.price

    return total_sum / len(phones)


def filter_by_brand(phones, brand):
    filtered_list = []
    target_brand = brand.lower()

    for phone in phones:
        if phone.brand.lower() == target_brand:
            filtered_list.append(phone)

    return filtered_list


all_phones = create_phone_list()

print("--- Всички телефони ---")
for p in all_phones:
    p.display_info()

print("\n" + "-"*30 + "\n")

expensive_phone = find_max_price_phone(all_phones)
if expensive_phone:
    print("--- Най-скъпият телефон е ---")
    expensive_phone.display_info()

avg_price = calculate_average_price(all_phones)
print(f"\nСредна цена на всички телефони: {avg_price:.2f} лв.")

print("\n" + "-"*30 + "\n")

user_brand = input("Въведете марка за търсене (напр. Samsung): ")
found_phones = filter_by_brand(all_phones, user_brand)

print(f"\n--- Резултати за марка '{user_brand}' ---")
if found_phones:
    for p in found_phones:
        p.display_info()
else:
    print("Няма намерени телефони от тази марка.")
