#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Aoc 2022 - 02

import sys
sys.path.append('..')
import utils

ISSUE=2

def rock_paper_scissors(player1:int, player2:int) -> int:
	'''
	in: 1=rock, 2=paper, 3=scissors
	out: -1=player1 wins, 0=draw, 1=player2 wins
	'''
	if player1==player2:
		return 0
	rules = {
		3:2,
		2:1,
		1:3
	}
	if rules[player1]==player2:
		return -1
	else:
		return 1

def get_round_score(opponent:str, you:str) -> int:
	score = 0
	values_opp = " ABC"
	turn_opp = values_opp.find(opponent)
	values_you = " XYZ"
	turn_you = values_you.find(you)
	if turn_opp>0 and turn_you>0:
		outcome = rock_paper_scissors(turn_opp, turn_you) # -1,0,1
		score_round = turn_you + (outcome + 1) * 3
		# ~ print([turn_opp, turn_you, outcome, score_round])
		score = score_round
	return score

"""
	SOLVE PART 1
"""
def solve_part_1(demo:bool) -> str:

	fn = utils.get_input_file(demo, ISSUE)
	print(fn)
	"""Do something here >>>"""

	rounds = utils.read_file_into_list(fn, lambda line: tuple(line.strip().split(' ')))
	# ~ print(rounds)

	score = 0
	for gr in rounds:
		# gr as "game round"
		score += get_round_score(gr[0], gr[1])

	answer = score

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

	rounds = utils.read_file_into_list(fn, lambda line: tuple(line.strip().split(' ')))
	# ~ print(rounds)

	score = 0
	for gr in rounds:
		# gr as "game round"
		score += get_round_score2(gr[0], gr[1])

	answer = None

	"""<<< Do something here"""
	utils.print_answer(2, demo, answer)
	return answer

"""
	MAIN
"""
def main(args):

	solve_part_1(0)

	# ~ solve_part_2(1)

	return 0

if __name__ == '__main__':
	sys.exit(main(sys.argv))
