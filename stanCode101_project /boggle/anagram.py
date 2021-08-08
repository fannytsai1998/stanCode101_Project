"""
File: anagram.py
Name: Fanny Tsai
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dict_list = []


def main():
    """
    Find all anagram that user entered
    """
    start = time.time()
    ####################
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        else:
            find_anagrams(s)

    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    global dict_list
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip('\n')
            dict_list.append(line)
    return dict_list


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    print('Searching....')
    all_ans = find_anagrams_helper(s, [], len(s), [], '')
    print(str(len(all_ans))+' anagrams: ', end='')
    print(all_ans)


def find_anagrams_helper(s, current_s, ans_s, all_ans, index):
    if len(current_s) == ans_s:
        ans = ''
        for ch in current_s:
            ans += ch
        if ans in dict_list:
            if ans not in all_ans:
                all_ans.append(ans)
                if len(all_ans) == 1:
                    print('Found: ' + ans)
                else:
                    print('Searching....')
                    print('Found: ' + ans)
    else:
        for i in range(len(s)):
            if str(i) not in index:
                # choose
                index += str(i)
                current_s.append(s[i])
                # turn into string
                sub = ''
                for char in current_s:
                    sub += char
                # find if sub string in dict
                if has_prefix(sub):
                    # explore
                    find_anagrams_helper(s, current_s, ans_s, all_ans, index)
                # un-choose
                # Index 也要 un-choose
                index = index[:-1]
                current_s.pop()
    return all_ans


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for sub in dict_list:
        if sub.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
