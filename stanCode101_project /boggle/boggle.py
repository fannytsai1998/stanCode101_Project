"""
File: boggle.py
Name: fanny tsai
----------------------------------------
TODO: find all possible word in boggle
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'test.txt'

def main():
	"""
	Find all match word on a 4*4 boggle, and follow the game rule.
	"""

	####################
	# input 4 rows by input format
	while True:
		row_1 = input('1 row of letters: ').lower()
		if check_row_format(row_1) == 'exit':
			print('Illegal input')
			print('Retype row 1 again with correct input format! ')
		else:
			lis_1 = row_1.split()
			break
	while True:
		row_2 = input('2 row of letters: ').lower()
		if check_row_format(row_2) == 'exit':
			print('Illegal input')
			print('Retype row 2 again with correct input format! ')
		else:
			lis_2 = row_2.split()
			break
	while True:
		row_3 = input('3 row of letters: ').lower()
		if check_row_format(row_3) == 'exit':
			print('Illegal input')
			print('Retype row 3 again with correct input format! ')
		else:
			lis_3 = row_3.split()
			break
	while True:
		row_4 = input('4 row of letters: ').lower()
		if check_row_format(row_4) == 'exit':
			print('Illegal input')
			print('Retype row 4 again with correct input format! ')
		else:
			lis_4 = row_4.split()
			break
	start = time.time()
	# all input alphabet
	all_s = row_1 + row_2 + row_3 + row_4
	# all_s = 'f y c l i o m g o r i l h j h u '
	# 4*4 boggle list of list
	lis_all = [lis_1, lis_2, lis_3, lis_4]
	# lis_all = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]
	# list all possible option in Boggle
	# mapping w create dict
	find_boggle(lis_all, all_s)
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')
	####################


def check_row_format(row):
	# row deleted last the possible space is over 7 digit
	if len(row.strip()) != 7:
		return 'exit'
	else:
		for i in range(4):
			if i % 2 == 0:  # even 偶數index的字，須為英文字母
				if not row[i].isalpha or len(row[i]) > 1:
					return 'exit'
			else:
				if row[i] != ' ':  # odd is space, can't be , ! .
					return 'exit'


def read_dictionary(s):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python dict
	dic = { 'd': ['dog','dance','dummy',....], 'f':['funny',fast','fraud'....] }
	"""
	# use the 16 char that user input to create a possible word dict.
	word_dict = {}
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			# only the word have more than 4 character
			if word[0] in s and len(word) >= 4:
				if word[0] in word_dict:
					word_dict[word[0]].append(word)
				else:
					word_dict[word[0]] = [word]
	return word_dict


def find_boggle(lis_all, all_s):
	"""
	:param lis_all: a list of list contains 16 character user input.
	:param all_s : all 16 character in a string???
	:return: possible combinations of 16 character
	"""
	cur_l = []
	dic = read_dictionary(all_s)
	lst = []
	# 因為有16個子母 -> 16種開頭的方式
	for i in range(4):
		for j in range(4):
			# 選擇一個開頭座標 ＝ 字母
			start_x = int(i)
			start_y = int(j)
			lst = find_boggle_helper(lis_all, start_x, start_y, '', cur_l, [], dic)
	print('There are',len(lst), 'words in total.')


def find_boggle_helper(lis_all, x, y, current_s, cur_l, index, p_dict):
	"""
	:param lis_all: list of list
	:param x: index of x
	:param y: index of y
	:param current_s: string
	:param cur_l: store answer
	:param index: list of tuple
	:param p_dict : possible dictionary
	"""

	if len(current_s) == 4:
		if current_s not in cur_l:
			if current_s in p_dict[current_s[0]]:
				cur_l.append(current_s)
				print('Found \" '+current_s+' \"')
				# for word in p_dict[current_s[0]]:
				# 	word.startswith(current_s)
				# 	find_boggle_helper_long(lis_all, index[-1][0], index[-1][1], current_s, cur_l, index, p_dict)
	if len(current_s) == 5:
		if current_s not in cur_l:
			if current_s in p_dict[current_s[0]]:
				cur_l.append(current_s)
				print('Found \" '+current_s+' \"')
	else:
		# find neighbor
		for i in range(-1, 2, 1):
			for j in range(-1, 2, 1):
				nb_x = i + x
				nb_y = j + y
				if 0 <= nb_x < 4:
					if 0 <= nb_y < 4:
						# 濾除重複index
						if (nb_x, nb_y) not in index:
							# 可能字母
							nb = lis_all[nb_x][nb_y]
							# 可能字母之index tuple index x,y
							index.append((nb_x, nb_y))
							# choose
							current_s += nb
							# find if sun in dict, in order to shorten algorithm
							# explore
							if has_prefix(current_s, p_dict):
								find_boggle_helper(lis_all, nb_x, nb_y, current_s, cur_l, index, p_dict)
							# un-choose
							current_s = current_s[:-1]
							index.pop()
	return cur_l


def find_boggle_helper_long(lis_all, x, y, current_s, cur_l, index, p_dict ):
	if len(current_s) == 5:
		if current_s not in cur_l:
			if current_s in p_dict[current_s[0]]:
				cur_l.append(current_s)
				print('Found \" '+current_s+' \"')
	else:
		# find neighbor
		for i in range(-1, 2, 1):
			for j in range(-1, 2, 1):
				nb_x = i + x
				nb_y = j + y
				if 0 <= nb_x < 4:
					if 0 <= nb_y < 4:
						# 濾除重複index
						if (nb_x, nb_y) not in index:
							# 可能字母
							nb = lis_all[nb_x][nb_y]
							# 可能字母之index tuple index x,y
							index.append((nb_x, nb_y))
							# choose
							current_s += nb
							# find if sun in dict, in order to shorten algorithm
							# explore
							if has_prefix(current_s, p_dict):
								find_boggle_helper_long(lis_all, nb_x, nb_y, current_s, cur_l, index, p_dict)
							# un-choose
							current_s = current_s[:-1]
							index.pop()
	return cur_l



def has_prefix(sub_s, dic):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dic : a dictionary of possible word
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for key in dic:
		for word in dic[key]:			# choose sub dict start with initial character
			if word.startswith(sub_s):
				return True
	return False


if __name__ == '__main__':
	main()
