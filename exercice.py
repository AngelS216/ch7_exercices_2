#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


def get_fibonacci_number(index:int):
	'''if index == 0:
		nb_fibon = 0
	elif index == 1:
		nb_fibon = 1
	else:
		get_fibonacci_number(index-1) + get_fibonacci_number(index-2)'''
	return (0 if index == 0 else 1 if index == 1 else get_fibonacci_number(index-1) + get_fibonacci_number(index-2))

def get_fibonacci_sequence(taille: int) -> list:
	sequence = [0,1]
	if taille <= 2:
		sequence = sequence[0:taille]
	else:
		for i in range(2,taille):
			sequence.append(sequence[-1] + sequence[-2])
			#car le dernier elem de la liste est tjs égal à la somme des 2 élém qui le précèdent
	return sequence

def get_sorted_dict_by_decimals(dict_decimals):
	'''for key, value in dict_decimals.items():
		partie_decimal = value%1'''
	return dict(sorted(dict_decimals.items(), key=lambda x: x[1]%1, reverse=False))

def fibonacci_numbers(length):
	init_val = [0,1]
	val_now = 0
	for value in init_val[0:2]:
		yield value
	if length > 2:
		deux_derniers_elem = deque(init_val)
		for i in range(len(init_val),length):
			val_now = deux_derniers_elem[-1] + deux_derniers_elem[-2]
			deux_derniers_elem.append(val_now)
			deux_derniers_elem.popleft() #pcq ds l'instruction, il dit qu'il ne veut que garder les 2 derniers élém en mémoire
			yield val_now


def build_recursive_sequence_generator(initVal, formule, garde_vals = False):
	def generator(length):
		for value in initVal[0:length]:
			yield value
		derniers_elem = deque(initVal)
		for i in range(len(initVal),length):
			val_now = formule(derniers_elem)
			derniers_elem.append(val_now)
			if garde_vals == False:
				derniers_elem.popleft() #pcq ds l'instruction, il dit qu'il ne veut que garder les 2 derniers élém en mémoire
			yield val_now
	return generator

if __name__ == "__main__":
	print([get_fibonacci_number(0), get_fibonacci_number(1), get_fibonacci_number(2)])
	print([get_fibonacci_number(i) for i in range(10)])
	print()

	print(get_fibonacci_sequence(1))
	print(get_fibonacci_sequence(2))
	print(get_fibonacci_sequence(10))
	print()

	spam = {
		2: 2.1,
		3: 3.3,
		1: 1.4,
		4: 4.2
	}
	eggs = {
		"foo": 42.6942,
		"bar": 42.9000,
		"qux": 69.4269,
		"yeet": 420.1337
	}
	print(get_sorted_dict_by_decimals(spam))
	print(get_sorted_dict_by_decimals(eggs))
	print()

	for fibo_num in fibonacci_numbers(10):
		print(fibo_num, end=" ")
	print("\n")

	def fibo_def(last_elems):
		return last_elems[-1] + last_elems[-2]
	fibo = build_recursive_sequence_generator([0, 1], fibo_def)
	for fi in fibo(10):
		print(fi, end=" ")
	print("\n")

	lucas = build_recursive_sequence_generator([2,1],lambda derniers_elem: derniers_elem[-1] + derniers_elem[-2])
	print(f"Lucas : {[elem for elem in lucas(10)]}")
	perrin = build_recursive_sequence_generator([3,0,2], lambda derniers_elem: derniers_elem[-2]+derniers_elem[-3])
	print(f"Perrin : {[elem for elem in perrin(10)]}")
	hofstadter_q = build_recursive_sequence_generator([1,1], lambda derniers_elem: derniers_elem[-derniers_elem[-1]] + derniers_elem[-derniers_elem[-2]], True)
	print(f"Hofstadter-Q : {[elem for elem in hofstadter_q(10)]}")
