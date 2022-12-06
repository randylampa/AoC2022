#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2022 - 04

import sys
sys.path.append('..')
import utils

ISSUE=4

"""
	SOLVE PART 1
"""
def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE)
	print(fn)
	"""Do something here >>>"""

	# functional (good|mad)ness
	pairs = utils.read_file_into_list(fn, lambda line: tuple(map(lambda x: tuple(map(int, x.split('-'))), line.strip().split(','))))
	# ~ print(pairs)

	overlap_count = 0
	for pair in pairs:
		elf1 = pair[0]
		elf2 = pair[1]
		if elf1[0]<=elf2[0] and elf1[1]>=elf2[1] or elf2[0]<=elf1[0] and elf2[1]>=elf1[1]:
			# elf1 contains elf2 OR elf2 contains elf1
			overlap_count += 1

	answer = overlap_count

	"""<<< Do something here"""
	utils.print_answer(1, demo, answer)
	return answer

def section_do_overlap(sec1_bnd:tuple, sec2_bnd:tuple) -> bool:
	# retrun overlapping part boundaries (or none)
	# ~ print([sec1_bnd, sec2_bnd])
	if sec1_bnd[0]>sec2_bnd[1] or sec2_bnd[0]>sec1_bnd[1]:
		# disjunkt
		# ~ print([sec1_bnd, sec2_bnd, 'are disjunct'])
		return False
	return True

"""
	SOLVE PART 2
"""
def solve_part_2(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE)
	print(fn)
	"""Do something here >>>"""

	# functional (good|mad)ness
	pairs = utils.read_file_into_list(fn, lambda line: tuple(map(lambda x: tuple(map(int, x.split('-'))), line.strip().split(','))))
	# ~ print(pairs)

	overlap_count = 0
	for pair in pairs:
		if section_do_overlap(pair[0], pair[1]):
			overlap_count += 1

	answer = overlap_count

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
