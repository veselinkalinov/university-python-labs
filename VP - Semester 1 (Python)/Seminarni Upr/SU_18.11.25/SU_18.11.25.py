# Зад 1 - Има два баскетболни отбора (Team1 и Team2) в училище и те играят няколко мача всеки ден в зависимост от времето и интереса си. Някой ден играят по 3 мача, някой ден 2, някой ден 1 и т.н. Напишете функция на Python, FindDayWinner(), която приема като аргумент името на победителя от всеки мач и връща името на общия победител за деня. В случай на равен брой победи, върнете "Тіе".

def FindDayWinner(results):
    team1_wins = results.count("Team1")
    team2_wins = results.count("Team2")

    if team1_wins > team2_wins:
        return "Team1"
    elif team2_wins > team1_wins:
        return "Team2"
    else:
        return "Tie"


match_results = input()
day_winner = FindDayWinner(match_results)
print("The winner for the day is:", day_winner)

# Zad 2 -  Перфектното число е положително цяло число, което е равно на сумата от своите положителни делители. Напишете програма, която да отпечата всички перфектни числа, присъстващи в даден списък. За целта създайте функция checkPerfectNum(), която получава като аргумент цяло положително число въведено от потребителя. Функцията връща като резултат True ако числото е перфекто и False ако не е перфектно. Например, 28 е перфектно число, тъй като делителите на 28 са 1, 2, 4,7,14, сборът на неговите Делители е 1+2+4+7+ 14 = 28.


def checkPerfectNum(num):
    if num < 1:
        return False

    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i

    return divisors_sum == num


input_list = [6, 28, 12, 15, 496, 18, 20]
perfect_numbers = []
for number in input_list:
    if checkPerfectNum(number):
        perfect_numbers.append(number)
print("Perfect numbers in the list are:", perfect_numbers)

# Zad 3 - Дадено е двоично число и трябва да го преобразуваме в десетично, без да използваме библиотечна функция. Създайте функция, която получава като аргумент двоично число и връща резултат десетичния еквивалент на числото.


def BintoDecConverter(binary_str):
    decimal_value = 0
    binary_str = binary_str[::-1]

    for index, digit in enumerate(binary_str):
        if digit == '1':
            decimal_value += 2 ** index

    return decimal_value


binary_input = input("Enter a binary number: ")
decimal_output = BintoDecConverter(binary_input)
print("The decimal equivalent is:", decimal_output)

# Zad 4 - Дадено е десетично число и трябва да го преобразуваме в двуично, без да използваме библиотечна функция. Създайте функция, която получава като аргумент десетично число и връща резултат двуичния еквивалент на числото.


def DecToBinConverter(decimal_num):
    if decimal_num == 0:
        return '0'

    binary_str = ''
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_str = str(remainder) + binary_str
        decimal_num = decimal_num // 2

    return binary_str


decimal_input = int(input("Enter a decimal number: "))
binary_output = DecToBinConverter(decimal_input)
print("The binary equivalent is:", binary_output)

# Zad 5 - Напишете програма, в която се създава функция с два аргумента, явяващи се числови списъци въведени от потребителя. Резултатът се явява число равно на сумата от двойките произведения на елементите на списъците. Ако в един от списъците елементите са по-малко от другия, то недостигащите елементи се получават посредством циклично повторение на съдържанието на списъка.


def SumofLists(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    total_sum = 0

    for i in range(max(len1, len2)):
        elem1 = list1[i % len1]
        elem2 = list2[i % len2]
        total_sum += elem1 * elem2

    return total_sum


input_list1 = [1, 2, 3]
input_list2 = [4, 5]
result = SumofLists(input_list1, input_list2)
print("The sum of lists is:", result)

# Zad 6 - Напишете програма с функция с произволен брой числови аргументи, която връща като резултат списък от три елемента, средната, максималната и минималната стойност на аргументите.


def MinMaxAvg(*args):
    minimum = min(args)
    maximum = max(args)
    avg = round((sum(args)/len(args)), 2)

    return list[minimum, maximum, avg]


result = MinMaxAvg(16, 22, 12, 13, 45, 17)
print(result)

# Zad 7 - Напишете програма с функция с един текстов аргумент и произволен брой целочислени аргументи. Резултатът се явява текст, сформиран от буквите на първия текстов аргумент. Целочислените аргументи определят индексите на буквите, които трябва да влязат в текста резултат


def TextFromIndices(str_arg, *args):
    result = ''
    for index in args:
        if 0 <= index < len(str_arg):
            result += str_arg[index]
    return result


output = TextFromIndices("SeminarniUpr", 0, 2, 4, 6, 8)
print(output)

# Zad 8 - Дефинирайте функция, която намира НОК на две числа, функцията получава като аргумент две числа и връща резултат НОК на тези числа.

# Zad 9 - Напишете програма, която включва три функции - първата функция създава матрица с числа и я запълва със стойности, приема като аргумент броя редове и броя колони на матрицата, връща като резултат запълнената матрица, втората функция получава като аргумент матрицата и я принтира под формата на таблица, третата функция намира сумата по колони на матрицата с числа и я принтира за всяка колона поотделно.

# Zad 10 - Напишете програма, която проверява дали едно число може да бъде представено във вид на сумата от две прости числа. За целта създайте функция CheckPrime(), получаваща като аргумент цяло число и връщащо резултат True, ако числото е просто и False, ако не е просто.


def CheckPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def can_be_expressed_as_sum_of_two_primes(n):
    for i in range(2, n):
        if CheckPrime(i) and CheckPrime(n - i):
            return True
    return False


number = int(input("Enter a number: "))
if can_be_expressed_as_sum_of_two_primes(number):
    print(f"{number} can be expressed as the sum of two prime numbers.")
else:
    print(f"{number} cannot be expressed as the sum of two prime numbers.")
