# Zad.1

import random
import sys

mylst_15 = [random.randint(-sys.maxsize, -1)for _ in range(15)]
print(f"mylst_15:{mylst_15}")

max_value = max(mylst_15)
print(f"max_value:{max_value}")

sum_nums = 0
for x in mylst_15:
    sum_nums += x
print(f"sum_nums:{sum_nums}")

mylst_dev3 = [x for x in mylst_15 if x % 3 == 0]
mylst_dev3.sort()
print(f"mylst_dev3:{mylst_dev3}")

mylst_dev3 = mylst_dev3[::2]
