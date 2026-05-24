# --------------------------------------------------------------------------- #
#  File    : ft_water_reminder.py
#  Project : Python-00
#  Author  : jagan <jagan@student.42kl.edu.my>
#  Created : 2026/05/24 09:21
# --------------------------------------------------------------------------- #


def ft_water_reminder():
    day = int(input("Days since last watering: "))
    if (day > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
