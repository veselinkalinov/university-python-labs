# Zad 1
import random
while True:
    try:
        n = int(input("n(25<n<45):"))
        if 25 < n < 45:
            break
        else:
            print("n trqbva da e 25<n<45")
            continue
    except ValueError:
        print("Nevaliden vhod")
        continue

lst_1 = []
p = random.randint(-3700, -1600)
q = random.randint(2222, 3333)
print(f"\n--List1 trqbva da e v intervala:({p,q})--")
for i in range(n):
    while True:
        try:
            num = int(input(f"Chislo {i+1}(p<num<q)"))
            if p < num < q:
                lst_1.append(num)
                break
            else:
                print(f"num trqbva da e {p}<num<{q}")
                continue
        except ValueError:
            print("Nevaliden vhod")
            continue

print(f"List1:{lst_1}")

count_els = 0
for x in lst_1:
    if x > 0:
        stot = (x//100) % 10
        if stot % 2 == 0:
            count_els += 1
if count_els > 0:
    print(f"count_els:{count_els}")

min_index = None
min_value = None
for i in range(len(lst_1)):
    if lst_1[i] % 6 == 3:
        if min_value is not None or lst_1[i] < min_value:
            min_value = lst_1[i]
            min_index = i
if min_index is not None:
    print(f"min_value:{min_value}\nmin_index:{min_index}")

lst_2 = [x for x in lst_1 if 9 < abs(x) < 100 and x % 5 == 0]
print(f"List2:{lst_2}")

prod = 1
for i in range(len(lst_2)):
    if i % 2 != 0:
        prod *= lst_2[i]
if prod != 1:
    print(f"prod:{prod}")

for i in range(len(lst_2)):
    if lst_2[i] % 2 == 0 and i % 2 != 0:
        lst_2.pop(i)
        break

if len(lst_1) != len(lst_2):
    if len(lst_1) < len(lst_2):
        i = len(lst_1)//2
        new_el = lst_1[0]+lst_1[-1]
        lst_1.insert(i, new_el)
    else:
        n = len(lst_2)//2
        new_el2 = lst_2[0]+lst_2[-1]
        lst_2.insert(n, new_el2)

# Zad 2


class ClothesShop:
    def __init__(self, clothe_type, brand, price, quantity, size):
        self.clothe_type = clothe_type
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.size = size

    def sale(self, quantity):
        if self.quantity > quantity:
            self.quantity -= quantity
        else:
            print("Nqma nalichnost")

    def discount(self):
        if 1 < self.quantity <= 3:
            self.price -= self.price*0.35
        elif 4 < self.quantity <= 6:
            self.price -= self.price*0.15
        elif 6 < self.quantity:
            self.price = self.price

    def display_info(self):
        print(
            f"clothe_type:{self.clothe_type}\nbrand:{self.brand}\nprice:{self.price}\nquantity:{self.quantity}\nsize:{self.size}")


clothes_list = []
k = int(input("Broi produkta:"))
for i in range(k):
    print(f"\nProdukt {i+1}")
    clothe_type = input("clothe_type:")
    brand = input("brand:")
    price = int(input("price:"))
    quantity = int(input("quantity:"))
    size = int(input("size:"))
    clothes_list.append(ClothesShop(clothe_type, brand, price, quantity, size))


def search_by_size_type(clothes, num, type):
    sum_price = 0
    for c in clothes:
        sum_price += c.price
    avg = round((sum_price/len(clothes_list)), 2)
    num_type = [c for c in clothes if c.size ==
                num and c.clothe_type.lower() == type.lower() and c.price < avg]
    return num_type


def cheapest_clothes(clothes, br):
    found = False
    min_price = None
    min_brand = None
    min_item = None
    for c in clothes:
        if c.brand == br:
            found = True
            if min_price is None or c.price < min_price:
                min_price = c.price
                min_brand = c.brand
                min_item = c
    min_item.display_info()
    if not found:
        print("brand is not available")
        c.display_info()


def delete_by_type(clothes, typ):
    found = False
    for c in clothes:
        if c.quantity < 2:
            if c.clothe_type == typ:
                found = True
                clothes.remove(c)
    if not found:
        print("Nqma takiva artikuli")


def sort_clothes(clothes):
    clothes.sort(key=lambda x: x.price, reverse=True)
    for c in clothes:
        c.display_info()
