import random

#Създаване на списък
list = [1,2,3,4,5]
print(list)


#Създаване на списък с числа въведени от потребител
list = []
for i in range(5):
    x = int(input(f"{i+1}:"))
    list.append(x)
print(list)


#Създаване на списък със случайни числа
list = []
for i in range(5):
    list.append(random.randint(-10,10))
print(list)


#Сумиране на елементите в списък
sum=0
for i in range(len(list)):
    sum+=list[i]
print("sum = ",sum)


#Събиране на индексите на списъка
sum=0
for x in list:
    sum += x
print("sum = ",sum)


#Принтиране на най-малкото число
print("min = ",min(list))
#Принтиране на най-голямото число
print("max = ",max(list))


#Разделяне на елементите на списъка със ","
newlist=input().split(",")
print(newlist)


#Добавяне на подсписък в списъка като елемент
newlist.append([1,2,3])  # type: ignore
print(newlist)


#Добавяне на подсписъци в списъка като елементи
newlist=[[1,2,3],
         [11,12,13],
         [-1,-2,-3]]
print(newlist)


#Печатане на подсписъците на отделни редове
for x in newlist:
    print(x)
#Печатане на елементите на подсписъците на отделни редове
for x in newlist:
    for y in x:
        print(y,end="")
    print()


print(list)
print(list[1]) # <- Принтира се втория елемент на списъка
print(list[-1]) # <- Принтира се последния елемент на списъка
print(list[-2]) # <- Принтира се предпоследния елемент
#print(list[10]) <- IndexError: list index out of range

print(list)
#Slices
print(list[1:3]) # <- Принтира елементите след първия до третия
print(list[1:]) # <- Принтира елементите след първия до края
print(list[:4]) # <- Принтира всички елементи до четвъртия
print(list[-2:]) # <- Принтира предпоследния и последния елемент
print(list[:-3]) # <- Принтира всички елементи до пред предпоследния елемент
print(list[-2:-4]) # <- Принтира от предпоследния до пред пред предпоследния елемент
print(list[-4:-2]) # <- Принтира от пред пред предпоследния до предпоследния елемент
print(list[:]) # <- Принтира целия списък


list[1] = [11,12,13] # <- Променя първия елемент
print(list)

list += [-1,-2,-3] # <- Добавя елемент
print(list)

del list[0] # <- Изтрива елемент
print(list)

del list[2:4] # <- Изтрива елемент в област
print(list)

del list[:] # <- Изтрива всички елементи в списъка
list.clear() # <- Изтрива всички елементи в списъка
print(list)

del list # <- Изтрива списъка
#print(list) <- NameError: name "list" in not defined

list = []
for i in range(5):
    list.append(random.randint(-10,10))

list += [1,1] # <- Добавя се подсписък
print(list)

print(list.count(1)) # <- Брои елементите, които са равни на 1
print(list.index(1)) # <- Изкарва индекса на първия срещнат елемент, който е равен на 1

list.insert(0,[1,1]) # <- Вмъква се елемент на определена позиция
print(list)

list[0] += [2,2] # <- Вмъква се елемент накрая
print(list)

#list[3] += [2,2] <- TypeError: unsupported operant type(s) for += int and list
print(list)

list.remove(1) # <- Премахва първия елемент, който е равен на 1
print(list)

list.remove(11) # <- ValueError

if 1 in list: # <- Проверява се дали в списъка има елемент със стойност 1
    list.remove(1) # <- Премахва първия елемент, който е равен на 1

print(8>>1) # <- Числото 8 се дели на 2 на степен 1 (получава се 4)
print(-8>>2) # <- Числото -8 се дели на 2 на степен 2 (получава се -2)

print(8<<2) # <- Числото 8 се умножава на 2 на степен 1 (получава се 16)
print(-8<<2) # <- Числото -8 се умножава на 2 на степен 2 (получава се 32)
