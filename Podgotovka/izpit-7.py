# Zad.1

import random
while True:
    try:
        n = int(input("n(20<n<30):"))
        if 20 < n < 30:
            break
        else:
            print("n ne izpulnqva uslovieto 20<n<30")
            continue
    except ValueError:
        print("Nevaliden vhod")

list1 = [random.randint(-1000, 1000) for _ in range(n)]
print(f"List1:{list1}")

sum_odd = 0
for i in range(len(list1)):
    if i % 2 != 0:
        sum_odd += list1[i]
if sum_odd > 0:
    print(f"sum_odd:{sum_odd}")

count_br = 0
for x in list1:
    el_deset = (abs(x)//10) % 10
    if el_deset % 3 == 0:
        count_br += 1
if count_br > 0:
    print(f"count_br:{count_br}")

prod = 1
for x in list1:
    if x < 0 and x % 2 == 0:
        prod *= x
if prod != 1:
    print(f"prod:{prod}")

list2 = [x for x in list1 if x > n or x < -n]
print(f"List2:{list2}")

diff = max(list2)-min(list2)
print(f"diff:{diff}")

list_odd = []
count_odd = 0
for x in list2:
    if x % 2 != 0:
        list_odd.append(x)
        count_odd += 1
if count_odd > 0:
    print(f"Nechetni chisla v list2:{list_odd}\nTehniqt broi:{count_odd}")

min_value2 = None
for x in list2:
    if x < 0:
        if min_value2 is None or x < min_value2:
            min_value2 = x
if min_value2 is not None:
    list2.remove(min_value2)
    print(f"Premahnat e min_value:{min_value2}\nList2:{list2}")

# Zad.2


class Car:
    def __init__(self, car_brand, car_model, car_price, car_color, manifacture_year):
        self.car_brand = car_brand
        self.car_model = car_model
        self.car_price = car_price
        self.car_color = car_color
        self.manifacture_year = manifacture_year

    def display_info(self):
        print(f"Car Brand:{self.car_brand}\nCar Model:{self.car_model}\nCar Price:{self.car_price}\nCar Color:{self.car_color}\nManifacture Year:{self.manifacture_year}")


cars = []
while True:
    try:
        n = int(input("Broi koli:"))
        break
    except ValueError:
        print("Nevaliden vhod")

for i in range(n):
    while True:
        try:
            print(f"\n--Kola {i+1}--")
            car_brand = input("Car Brand:")
            car_model = input("Car Model:")
            car_price = int(input("Car Price"))
            car_color = input("Car Color:")
            manifacture_year = int(input("Manifacture Year:"))
            cars.append(Car(car_brand, car_model, car_price,
                        car_color, manifacture_year))
            break
        except ValueError:
            print("Nevaliden vhod")
            continue


def sort_price(car):
    car.sort(key=lambda x: x.car_price, reverse=True)
    for c in cars:
        c.display_info()


def list_by_brand(car, brand):
    found = False
    for c in car:
        if c.car_brand.lower() == brand.lower():
            found = True
            c.display_info()
    if not found:
        print("Nqma takava marka avtomobil")


def search_color(car, color):
    found = False
    most_expensive = None
    for c in car:
        if c.car_color.lower() == color.lower():
            found = True
            if most_expensive is None or c.car_price > most_expensive.car_price:
                most_expensive = c
    if not found:
        print("Nqma takuv cvqt avtomobil")
    return most_expensive


def newest_car(car):
    found = False
    newest = []
    for c in car:
        if c.manifacture_year == 2022:
            found = True
            newest.append(c)
    if not found:
        print("Nqma koli proizvedeni prez 2022")
    return newest
