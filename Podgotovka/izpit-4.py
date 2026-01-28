# Zad.1

import random

while True:
    try:
        n = int(input("n(20<n<40):"))
        if 20 < n < 40:
            break
        else:
            print("n trqbva da otgovarq na 20<n<40")
            continue
    except ValueError:
        print("Nevaliden vhod")

list1 = [random.randint(2, 200) for _ in range(n)]
print(f"List1:{list1}")

min_value = min(list1)
list1.remove(min_value)
print(f"Iztrit e element: {min_value}\nList1:{list1}")

sum_even = 0
for i in range(len(list1)):
    if i % 2 == 0:
        sum_even += list1[i]
print(f"Sumata e: {sum_even}")

count_els = 0
for x in list1:
    num_ed = (x//1) % 10
    if num_ed == 0:
        count_els += 1
if count_els > 0:
    print(f"count_els: {count_els}")

list2 = [x for x in list1 if (x % 3 == 0 or x %
         4 == 0) and not (x % 4 == 0 and x % 3 == 0)]
print(f"List2:{list2}")

count_odd = 0
sum_odd = 0
for x in list2:
    if x % 2 != 0:
        count_odd += 1
        sum_odd += x
if count_odd > 0:
    print(f"Avg:{round((sum_odd/count_odd),2)}")

max_value = None
max_index = None
for i in range(len(list2)):
    if max_value is None or list2[i] > max_value:
        max_value = list2[i]
        max_index = i
print(f"max_value:{max_value}\nmax_index:{max_index}")
