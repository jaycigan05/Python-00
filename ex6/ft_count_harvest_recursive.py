# --------------------------------------------------------------------------- #
#  File    : ft_count_harvest_recursive.py
#  Project : Python-00
#  Author  : jagan <jagan@student.42kl.edu.my>
#  Created : 2026/05/24 09:40
# --------------------------------------------------------------------------- #


def	ft_count_harvest_recursive():
	total = int(input("Days until harvest: "))

	def	countdown(current):
		if (current > total):
			print("Harvest time!")
			return
		print("Day", current)
		countdown(current + 1)
	countdown(1)
