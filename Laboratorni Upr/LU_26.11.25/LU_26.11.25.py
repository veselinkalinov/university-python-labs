# Зад 1. Напишете код на метод, който приема като параметър текстов файл, чете съдържанието на файла и го обръща в стринг.

import math


def read_file_to_string(file_path):
    try:
        with open(file_path) as file:
            content = file.read()

            # Check if content is empty string
            if not content:
                # We manually trigger an error here
                raise ValueError("Empty File")

        return content

    except FileNotFoundError:
        return "Грешка: Файлът не е намерен."

    except ValueError:
        return "Грешка: Файлът е празен (няма съдържание)."

    except Exception as e:
        return f"Грешка: {e}"


path = r"C:\Users\vesko\Documents\ТУ - София\VP\Laboratorni Upr\LU_26.11.25\txt_file.txt"
print(read_file_to_string(path))

# Зад.2 - Напишете програма, която прочита от конзолата цяло положително число и отпечатва корен квадратен на това число. Ако числото е отрицателно или невалидно да се изпише InvalidNumber и във всички случаи накрая да се изпише Goodbye.


def calculate_square_root():
    """
    Funksiia za chetene na chislo i izchislyavane na negovya koren kvadraten.
    Obrabotva greshki i vinagi otpechatva 'Goodbye' nakraya.
    """
    try:
        # Chetene na vhod ot potrebitelya
        user_input = input("Vavedete tsyalo polozhitelno chislo: ")
        number = int(user_input)

        if number < 0:
            print("InvalidNumber")
        else:
            sqrt_number = math.sqrt(number)
            # Formatirane do 2 znaka sled zapetayata za po-dobra chetimost,
            # ili prosto izvezhdane, kakto e v originala:
            print(f"Koren kvadraten na {number} e {sqrt_number:.2f}")

    except ValueError:
        print("InvalidNumber")
    finally:
        print("Goodbye")


# Izvikvane na funktsiyata
if __name__ == "__main__":
    calculate_square_root()
