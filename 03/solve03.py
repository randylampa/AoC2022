#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2022 - 03

import sys
sys.path.append('..')
import utils

ISSUE=3

def parse_rucksack_compartments(rucksack:str) -> tuple:
	rucksack = rucksack.strip()
	n = len(rucksack)
	return (rucksack[slice(0,n//2)], rucksack[slice(n//2,n)])

def get_item_priority(item:str) -> int:
	ord_ct = ord(item)
	if ord_ct>90:
		# should be (a-z)=(1-26)
		priority = ord_ct-ord('a')+1
	else:
		# should be (A-Z)=(27-52)
		priority = ord_ct-ord('A')+27
	return priority

"""
	SOLVE PART 1
"""
def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE)
	print(fn)
	"""Do something here >>>"""

	rucksack_compartments = utils.read_file_into_list(fn, parse_rucksack_compartments)
	# ~ print(rucksack_compartments)

	priority_sum = 0
	for rc in rucksack_compartments:
		# rc as "rucksack_compartment"
		common_types = list(set(rc[0]) & set(rc[1]))
		# ~ print([rc, common_types])
		for ct in common_types:
			priority_sum += get_item_priority(ct)

	answer = priority_sum

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer

# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
	# looping till length l
	for i in range(0, len(l), n):
		yield l[i:i + n]

"""
	SOLVE PART 2
"""
def solve_part_2(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE)
	print(fn)
	"""Do something here >>>"""

	rucksacks = utils.read_file_into_list(fn)
	# ~ print(rucksacks)

	priority_sum = 0
	for group in divide_chunks(rucksacks, 3):
		common_type = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
		# ~ print(group, common_type)
		priority_sum += get_item_priority(common_type)

	answer = priority_sum

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

"""
	MAIN
"""
def main(args):

	# ~ solve_part_1(0)

	solve_part_2(0)

	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
