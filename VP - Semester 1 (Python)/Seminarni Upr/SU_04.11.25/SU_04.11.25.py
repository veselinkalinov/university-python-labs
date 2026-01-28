import sys
import random
# Зад.1 - Напишете програма, в която потребителя въвежда две числа, а програмата определя цифрите, които са общи в представянията на двете числа.

num1 = input("Въведете първото число: ")
num2 = input("Въведете второто число: ")

common_digits = set(num1) & set(num2)
common_digits = [d for d in common_digits if d.isdigit()]

if common_digits:
    print("Общите цифри са:", ', '.join(sorted(common_digits)))
else:
    print("Няма общи цифри.")

# Зад.2 - Напишете програма за намиране на множество числа в интервала от М до Н, които се делят или на 3, или на 4. но да не се делят на 3 и на 4 едновременно.

m = int(input("Въведете М: "))
n = int(input("Въведете N: "))
result = []
for num in range(m, n+1):
    if ((num % 3 == 0 or num % 4 == 0) and not (num % 3 == 0 and num % 4 == 0)):
        result.append(num)
print(
    f'Числата в интервала от {m} до {n}, които изпълняват условието са {result}')

# Зад.3 - Програма, в която потребителят трябва да въведе текстова стойност. На основата на текста се формира речник, с ключове символите на този текст, а стойността представлява изходният текст с изтрит символът, който се явява ключът(ключовете не се повтарят).

text = input("Въведете текст: ")

result = {}

for char in list(text):
    result[char] = text.replace(char, "")

print("Речник:")
for k, v in result.items():
    print(f"'{k}': '{v}'")

# Зад.4 - Програма, в която на основата на текст, въведен от потребителят, се създава кортеж(tuple). На основата на, който се създава нов кортеж, в него се включват равностоящите елементи, започвайки от първия(с нулев индекс). Разстоянието между елементите се въвежда от потребителя

st = input("Enter string: ")
dis = int(input("Enter distance: "))
t = tuple(st)
t1 = tuple(t[::dis])
print(f"The first tuple is: {t}. \nThe second tuple is: {t1}")

# Зад.5 - Програма, в която потребителят запълва списък с числа. После се създава втори списък, който се състои от два елемента: стойността на втория по големина елемент в списъка и индекса на този елемент в списъка.

numbers = list(
    map(int, input("Въведете числа, разделени с интервал: ").split()))

unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
second_largest = unique_numbers[1]

index = numbers.index(second_largest)

result = [second_largest, index]

print("Вторият списък е:", result)

# Зад.6 - Програма, в която се създава числов списък, който се запълва със случайни числа. Елементите с четни индекси се сортират по възходящ ред, а елементите с нечетни индекси се сортират в низходящ ред. Принтирайте първият и новият списък.

n = int(input("Въведете брой елементи: "))
numbers = [random.randint(1, sys.maxsize) for _ in range(n)]

print("Оригинален списък:")
print(numbers)

even_index_elements = [numbers[i] for i in range(0, n, 2)]
odd_index_elements = [numbers[i] for i in range(1, n, 2)]

even_index_elements.sort()             # възходящ ред
odd_index_elements.sort(reverse=True)  # низходящ ред

sorted_numbers = []
even_idx, odd_idx = 0, 0
for i in range(n):
    if i % 2 == 0:
        sorted_numbers.append(even_index_elements[even_idx])
        even_idx += 1
    else:
        sorted_numbers.append(odd_index_elements[odd_idx])
        odd_idx += 1

print("Нов списък:")
print(sorted_numbers)
