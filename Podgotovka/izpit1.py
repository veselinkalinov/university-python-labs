# Zad 1

import random

while True:
    try:
        n = int(input("n(10<n<50):"))
        if 10 < n < 50:
            break
        else:
            print("n trqbva da otgovarq na uslovieto 10<n<50")
            continue
    except ValueError:
        print("Nevaliden vhod")

a = random.randint(-2500, -1300)
b = random.randint(1111, 4444)
print(f"mylst_1 trqbva da e v interval: [{a,b}]")

mylst_1 = []
for i in range(n):
    while True:
        try:
            nums = int(input(f"Chislo {i+1}:"))
            if a <= nums <= b:
                mylst_1.append(nums)
                break
            else:
                print(f"nums trqbva da e v interval:{a,b}")
                continue
        except ValueError:
            print("Nevaliden vhod")

print(f"mylst_1:{mylst_1}")

count_br = 0
for x in mylst_1:
    if x < 0:
        el_deset = (abs(x)//10) % 10
        if el_deset % 4 == 0 or el_deset % 5 == 0:
            count_br += 1
if count_br > 0:
    print(f"count_br:{count_br}")

count_el = 0
sum_el = 0
for x in mylst_1:
    if 9 < abs(x) < 100 and x % 2 == 0:
        count_el += 1
        sum_el += x
if count_el > 0:
    print(f"Avg:{round((sum_el/count_el),2)}")

mylst_2 = [x for x in mylst_1 if 99 < abs(x) < 1000 and x % 3 == 0]
print(f"mylst_2:{mylst_2}")

count_odd = 0
for i in range(len(mylst_2)):
    if i % 2 == 0 and mylst_2[i] % 2 != 0:
        count_odd += 1
if count_odd > 0:
    print(f"count_odd:{count_odd}")

for i in range(len(mylst_2)):
    if i % 2 != 0:
        mylst_2[i] = 13
print(f"mylst_2(13):{mylst_2}")

if len(mylst_1) != len(mylst_2):
    if len(mylst_1) > len(mylst_2):
        mylst_1.pop()
        mylst_1.pop(0)
    else:
        mylst_2.pop()
        mylst_2.pop(0)
print(f"Lists after pop operation:\nList1:{mylst_1}\nList2:{mylst_2}")

# Zad 2


class Market:
    def __init__(self, barcod, name, manufacturer, price, quantity):
        self.barcod = barcod
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.quantity = quantity

    def sale(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
            return quantity
        else:
            return 0

    def discount(self):
        if 30 <= self.price <= 50:
            discount = self.price*0.05
        elif 10 <= self.price < 30:
            discount = self.price*0.07
        else:
            discount = 0
        return discount

    def display_info(self):
        print(
            f"Barcod:{self.barcod}\nName:{self.name}\nManufacurer:{self.manufacturer}\nPrice:{self.price}\nQuantity:{self.quantity}")


product_list = []
while True:
    try:
        n = int(input("Broi produkti:"))
        break
    except ValueError:
        print("Nevaliden vhod")
        continue

for i in range(n):
    while True:
        try:
            print(f"\n--Produkt {i+1}--")
            barcod = int(input("Barcod:"))
            name = input("Name:")
            manufacturer = input("Manufacturer:")
            price = int(input("Price:"))
            quantity = int(input("Quantity:"))
            product_list.append(
                Market(barcod, name, manufacturer, price, quantity))
            break
        except ValueError:
            print("Nevaliden vhod")
            continue


def search_by_barcod(products, pbarcod):
    found = False
    for p in products:
        if p.barcod == pbarcod:
            found = True
            p.display_info()
            break
    if not found:
        print("Wrong barcode!!!")
        print("Available barcodes:", [p.barcod for p in products])


def search_by_manufacturer(products, pmanufacturer):
    manuf_products = [
        p for p in products if p.manufacturer.lower() == pmanufacturer.lower()]

    if not manuf_products:
        return []

    avg_price = sum(p.price for p in manuf_products) / len(manuf_products)

    result_list = [p for p in manuf_products if p.price <= avg_price]

    return result_list


def sort_by_quantity(products):
    products.sort(key=lambda x: x.quantity, reverse=False)
    for p in products:
        p.display_info()


def delete_by_name(products, pname):
    found = False
    for p in products:
        if p.name.lower() == pname.lower():
            found = True
            if p.quantity <= 3:
                products.remove(p)
    if not found:
        print("Nqma takuv produkt")
