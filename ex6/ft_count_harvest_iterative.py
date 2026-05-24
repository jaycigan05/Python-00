# --------------------------------------------------------------------------- #
#  File    : ft_count_harvest_iterative.py
#  Project : Python-00
#  Author  : jagan <jagan@student.42kl.edu.my>
#  Created : 2026/05/24 09:31
# --------------------------------------------------------------------------- #


def ft_count_harvest_iterative():
    day = int(input("Days until harvest: "))
    for i in range(1, (day + 1)):
        print("Day", i)
    print("Harvest time!")
