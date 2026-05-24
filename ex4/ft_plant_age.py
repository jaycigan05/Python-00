# --------------------------------------------------------------------------- #
#  File    : ft_plant_age.py
#  Project : Python-00
#  Author  : jagan <jagan@student.42kl.edu.my>
#  Created : 2026/05/24 09:05
# --------------------------------------------------------------------------- #


def ft_plant_age():
    day = int(input("Enter plant age in days: "))
    if (day > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
