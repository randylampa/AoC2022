#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2022 - 01

import sys
sys.path.append('..')
import utils

ISSUE=1

def parse_line(line:str):
	'''
	returns int|None
	'''
	x = line.strip()
	if x:
		return int(x)
	return None

def map_to_elves(cal_none:list) -> list:
	elves = []
	elf_calorie = 0
	for n in cal_none:
		if n is None:
			elves.append(elf_calorie);elf_calorie = 0;continue
		elf_calorie+=n
	if elf_calorie>0:
		# do not forget last one...
		elves.append(elf_calorie)
	return elves

"""
	SOLVE PART 1
"""
def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE)
	print(fn)
	"""Do something here >>>"""

	elf_calories = utils.read_file_into_list(fn, parse_line)
	# ~ print(elf_calories)

	elves = map_to_elves(elf_calories)
	# ~ print(elves)

	answer = max(elves)

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer

"""
	SOLVE PART 2
"""
def solve_part_2(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE)
	print(fn)
	"""Do something here >>>"""

	elf_calories = utils.read_file_into_list(fn, parse_line)
	# ~ print(elf_calories)

	elves = map_to_elves(elf_calories)
	# ~ print(elves)

	elves.sort(reverse=True)
	# ~ print(elves,elves[:3])

	answer = sum(elves[:3])

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
