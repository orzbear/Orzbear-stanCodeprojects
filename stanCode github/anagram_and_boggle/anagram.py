"""
File: anagram.py
Name:Cho-Han Hsiung
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

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop

# Global variables
d = []


def main():
    """
    This program recursively finds all the anagram(s)
    for the word input by user and terminates when the
    input string matches the EXIT constant defined
    at line 19.
    This function prints the number of anagrams and the list of anagrams.
    """
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    read_dictionary()
    while True:
        # Input the word to find anagrams
        s = input('Find anagrams for: ')
        start = time.time()
        if s == EXIT:
            # Set exit condition
            break
        else:
            # Recursion
            ans = find_anagrams(s)
        # Print result
        print(f'{len(ans)} anagrams: {ans}')
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    """
    :return: This function does not return anything
    This function import dictionary.txt as the list d.
    """
    with open(FILE, 'r') as f:
        for line in f:
            # Every line is a word
            line = line.strip()
            # delete the space and \n in before and after the word
            d.append(str(line))


def find_anagrams(s):
    """
    :param s: str, the word we input to find anagrams.
    :return: list of str, including all the anagrams which exists in our dictionary.
    This function transfer our word s into a dic, creating a smaller dictionary only includes the words with same
    length as s, searching if the word in anagram list exist in our dictionary, and running find_anagrams_helper to find
    anagrams.
    """
    # Transfer our word s into a dic, since there may be same characters in one word
    s_dic = {}
    for i in range(len(s)):
        ch = s[i]
        s_dic[i] = ch
    # Creating a smaller dictionary only includes the words with same length as s, since the anagrams will have the
    # same length
    d_smaller = []
    for word in d:
        if len(word) == len(s_dic):
            d_smaller.append(word)
    # Running the recursion to find all anagrams
    ans = find_anagrams_helper(s_dic, [], "", len(s_dic), [], d_smaller)
    # Searching if the word in anagram list exist in our dictionary
    for a in ans:
        if a in d_smaller:
            print("Searching...")
            print(f'Found: {a}')
        else:
            ans.remove(a)
    return ans


def find_anagrams_helper(s_dic, used, current_string, ans_len, ans, d_smaller):
    """

    :param s_dic: dic, key = int, 0 ~ len(s)-1, value: characters
    :param used: list, recording which characters we have already used
    :param current_string: str, recording our current string result
    :param ans_len: int, the length of our word
    :param ans: list, the list contains all anagrams
    :param d_smaller: list, a smaller dictionary only includes the words with same length as s
    :return: list, the list contains all anagrams
    """
    if len(current_string) == ans_len:
        # Base case: if our current string is as long as our word
        if current_string not in ans:
            # If there are same characters in a word, avoiding adding the same words
            ans.append(current_string)
    else:
        for ch_d in s_dic:
            if ch_d in used:
                pass
            else:
                # choose
                used.append(ch_d)
                current_string += s_dic[ch_d]
                # explore
                if has_prefix(current_string, d_smaller):
                    # Checking if there are words with our current string as prefix, only keep exploring if there is
                    # one.
                    find_anagrams_helper(s_dic, used, current_string, ans_len, ans, d_smaller)
                    # un-choose
                    used.pop()
                    current_string = current_string[:-1]
                else:
                    # if there are no words with our current string as prefix, stop explore and un-choose
                    used.pop()
                    current_string = current_string[:-1]
    return ans


def has_prefix(sub_s, d_smaller):
    """
    :param d_smaller: list, a smaller dictionary only includes the words with same length as s
    :param sub_s: str, our current string.
    :return: boolean, true or false.
    """
    for word in d_smaller:
        if str(word).startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
