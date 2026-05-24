# --------------------------------------------------------------------------- #
#  File    : ft_seed_inventory.py
#  Project : Python-00
#  Author  : jagan <jagan@student.42kl.edu.my>
#  Created : 2026/05/24 10:20
# --------------------------------------------------------------------------- #


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        print(seed_type.capitalize(), "seeds:", quantity, unit, "available")
    elif (unit == "grams"):
        print(seed_type.capitalize(), "seeds:", quantity, unit, "total")
    elif (unit == "area"):
        print(seed_type.capitalize(), "seed: cover", quantity, "square meters")
    else:
        print("Unknown unit type")
