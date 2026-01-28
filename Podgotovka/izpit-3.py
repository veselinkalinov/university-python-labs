# Zad.1

import random

while True:
    try:
        x = int(input("X(5<=x<=15):"))
        if 5 <= x <= 15:
            break
        else:
            print("x trqbva da izpulnqva uslovie 5<=x<=15")
            continue
    except ValueError:
        print("Nevaliden vhod")

list1 = [random.randint(50, 80) for _ in range(x)]
list2 = [random.randint(50, 80) for _ in range(x)]
print(f"List1: {list1}\nList2:{list2}")

list3 = [x for x in list1 if x in list2]
list3.sort(reverse=True)
print(f"List3:{list3}")

list4 = [x for x in list2 if x not in list1]
print(f"List4:{list4}")

count_num = 0
sum_num = 0
for x in list4:
    count_num += 1
    sum_num += x
print(f"Avg:{round((sum_num/count_num),2)}")

list4 = list4[::2]
