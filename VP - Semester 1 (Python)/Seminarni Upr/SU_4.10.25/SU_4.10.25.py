# Зад.1 - Да се напише програма, която въвежда последователност от цели числа от клавиатурата, потребителят определя броя елементи и ги записва в списък. Програмата да извърши следните обработки: отпечатва елементите на списъка един по един, изчислява сумата на елементите на списъка и извежда стойността ѝ, намира максималния и минималния елемент в списъка, сортира списъка, по зададен от потребителя индекс променя стойността на избран елемент от списъка.

n = int(input("Въведете брой елементи в списъка: "))
elements = []
for i in range(n):
    num = int(input(f"Въведете елемент {i+1}: "))
    elements.append(num)

print("Елементите на списъка са:")
for elem in elements:
    print(elem)

total_sum = sum(elements)
print(f"Сумата на елементите е: {total_sum}")
max_elem = max(elements)
min_elem = min(elements)
print(f"Максимален елемент: {max_elem}")
print(f"Минимален елемент: {min_elem}")
elements.sort()
print("Сортиран списък:", elements)
index = int(input("Въведете индекс на елемента, който искате да промените: "))
if 0 <= index < n:
    new_value = int(input("Въведете новата стойност: "))
    elements[index] = new_value
    print("Актуализиран списък:", elements)

# Зад.2 - Напишете програма на Python, която създава списък от n низове, въведени от потребителя, и извършва следните обработки: определя кой от записаните в списъка низове е с най-голяма дължина, замества избран низ с друг, въведен от потребителя, изтрива избран низ и въвежда нов низ на избрана позиция в списъка.

n = int(input("Въведете брой низове в списъка: "))
strings = []
for i in range(n):
    s = input(f"Въведете низ {i+1}: ")
    strings.append(s)
print("Низовете в списъка са:")
for string in strings:
    print(string)

max_length_string = max(strings, key=len)

index = int(input("Въведете индекс на елемента, който искате да промените: "))
if 0 <= index < n:
    new_string = input("Въведете новата стойност: ")
    strings[index] = new_string
    print("Актуализиран списък:", strings)
delete_index = int(
    input("Въведете индекс на елемента, който искате да изтриете: "))
if 0 <= delete_index < n:
    strings.pop(delete_index)
    print("Списък след изтриване:", strings)

insert_index = int(
    input("Въведете индекс, на който искате да вмъкнете нов низ: "))
if 0 <= insert_index <= len(strings):
    new_string = input("Въведете новия низ: ")
    strings.insert(insert_index, new_string)

print("Списък след вмъкване:", strings)
print(
    f"Низът с най-голяма дължина е: '{max_length_string}' с дължина {len(max_length_string)}")

# Зад.3 - Да се напише програма, която въвежда n двойки – ключ и цяло число за стойност от клавиатурата и ги записва в речник. Програмата да извърши следните обработки: търси по ключ в речника, променя стойността на елемент от речника по неговия ключ, изтрива елемент от речника по ключ, извежда всички ключове от речника, извежда всички стойности от речника, сортира речника по ключове. Извеждането на съдържанието на речника да се прави с обхождане на елементите му по ключ.
n = int(input("Въведете брой елементи в речника: "))
my_dict = {}
for i in range(n):
    key = input(f"Въведете ключ {i+1}: ")
    value = int(input(f"Въведете стойност за ключ '{key}': "))
    my_dict[key] = value
print("Съдържанието на речника е:")
for k in my_dict:
    print(f"{k}: {my_dict[k]}")
search_key = input("Въведете ключ за търсене: ")
if search_key in my_dict:
    print(f"Стойността за ключ '{search_key}' е: {my_dict[search_key]}")
change_key = input("Въведете ключ, чиято стойност искате да промените: ")
if change_key in my_dict:
    new_value = int(input("Въведете новата стойност: "))
    my_dict[change_key] = new_value
    print(
        f"Актуализирана стойност за ключ '{change_key}': {my_dict[change_key]}")
delete_key = input("Въведете ключ, който искате да изтриете: ")
if delete_key in my_dict:
    del my_dict[delete_key]
    print(f"Ключ '{delete_key}' е изтрит.")
print("Всички ключове в речника:", list(my_dict.keys()))
print("Всички стойности в речника:", list(my_dict.values()))
sorted_dict = dict(sorted(my_dict.items()))
print("Сортиран речник по ключове:")
for k in sorted_dict:
    print(f"{k}: {sorted_dict[k]}")

# Зад.4 - Напишете програма на Python, която създава две множества от m цели числа, въведени от потребителя, и извършва следните обработки: определя размера на двете множества, обединява двете множества, пресичане на двете множества, премахване на избран елемент от първо множество и изчисляване на двете множества.

m = int(input("Въведете брой елементи в множествата: "))
set1 = set()
set2 = set()
print("Въвеждане на елементи за първото множество:")
for i in range(m):
    num = int(input(f"Въведете елемент {i+1} за първото множество: "))
    set1.add(num)
print("Въвеждане на елементи за второто множество:")
for i in range(m):
    num = int(input(f"Въведете елемент {i+1} за второто множество: "))
    set2.add(num)
print(f"Размер на първото множество: {len(set1)}")
print(f"Размер на второто множество: {len(set2)}")
union_set = set1.union(set2)
print("Обединение на двете множества:", union_set)
intersection_set = set1.intersection(set2)
print("Пресичане на двете множества:", intersection_set)
remove_element = int(
    input("Въведете елемент от първото множество, който искате да премахнете: "))
if remove_element in set1:
    set1.remove(remove_element)
    print(
        f"Първото множество след премахване на елемента {remove_element}:", set1)
difference_set = set1.difference(set2)
print("Разлика между първото и второто множество:", difference_set)

# Зад.5 - Да се напише програма, която създава речник от 7 въведени от потребителя низа и съответстващите им цели числа и извършва следните обработки: разпечатва съдържанието на речника, определя на кой ключ съответства най - голямото въведено цяло число от записаните в речника, заменя стойността въведена за избран ключ с друга въведена от потребителя, изтрива стойност от речника по нейния клчюч и добавя нова стойност в речника заедно с нейния ключ.

my_dict = {}
for i in range(7):
    key = input(f"Въведете ключ {i+1}: ")
    value = int(input(f"Въведете стойност за ключ '{key}': "))
    my_dict[key] = value
print("Съдържанието на речника е:")
for k in my_dict:
    print(f"{k}: {my_dict[k]}")

max_key = max(my_dict, key=my_dict.get)
print(
    f"Ключът с най-голяма стойност е: '{max_key}' със стойност {my_dict[max_key]}")
change_key = input("Въведете ключ, чиято стойност искате да промените: ")
if change_key in my_dict:
    new_value = int(input("Въведете новата стойност: "))
    my_dict[change_key] = new_value
    print(
        f"Актуализирана стойност за ключ '{change_key}': {my_dict[change_key]}")

delete_key = input("Въведете ключ, който искате да изтриете: ")
if delete_key in my_dict:
    my_dict.pop(delete_key)
    print(f"Стойност с ключ '{delete_key}' е изтрита.")
my_dict.update({input("Въведете нов ключ за добавяне: ")
               : int(input("Въведете стойност за новия ключ: "))})
print("Актуализирано съдържание на речника:")
for k in my_dict:
    print(f"{k}: {my_dict[k]}")
