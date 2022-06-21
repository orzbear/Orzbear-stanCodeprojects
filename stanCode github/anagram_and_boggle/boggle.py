"""
File: boggle.py
Name:Cho Han Hsiung
* I have discussed this assignment with Kai-wen Tung, but we did not share our codes.
----------------------------------------
This program simulates boggle game using 16 letters entered by the users, and it will list all words in the matrix of
letters
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    This function simulates boggle game using 16 letters entered by the users, and it will list all words in the matrix of
    letters
    """
    letters = []
    letters_str = ""
    for i in range(4):
        s = input(f'{i + 1} rows of data: ')
        # Make sure the input follow our demands: only alphabets, case-insensitive and spaces between 4 characters.
        if s[1] != " " or s[3] != " " or s[5] != " " or s[0].isalpha() is False or s[2].isalpha() is False or \
                s[4].isalpha() is False or s[6].isalpha() is False:
            print("Illegal input")
            break
        else:
            # Creating each row as a string
            letters_str = str(s[0])+str(s[2])+str(s[4])+str(s[6])
            letters.append(letters_str)
    d = read_dictionary(letters)
    start = time.time()
    find_ans(letters, d)
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(letters):
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python

    :param letters: list of strings.
    :return: dic, key is the alphabet they start with.
    """
    d = {}
    with open(FILE, 'r') as f:
        for line in f:
            for row in letters:
                for ch in row:
                    # Every line is a word
                    line = line.strip()
                    # delete the space and \n in before and after the word
                    # only keep the word more than 4 characters
                    if len(line) >= 4:
                        # and only keep the words starts with the characters we input
                        if line.startswith(ch) and ch not in d:
                            d[ch] = [line]
                        elif line.startswith(ch) and ch in d:
                            d[ch].append(line)
    return d


def has_prefix(sub_s, d_l):
    """
    :param d_l: the smaller dic only includes the words start with specific characters
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in d_l:
        if str(word).startswith(sub_s):
            return True
    return False


def find_ans(letters, d):
    """
    This function finds the answers of boggle.
    :param letters:list of strings(letters included).
    :param d: dic, the key is the alphabets we entered and the value are list of words
    :return: None
    """
    # Empty list ot save the answers
    ans = []
    # There are total 16 letters to start with, 4 rows and there are 3 letters in each row
    for i in range(4):
        for j in range(4):
            # Recording what letters we have used
            used = []
            # Recording our starting letter
            start = letters[i][j]
            used.append([i, j])
            # Only need to find the words start with our starting letter.
            d_l = d[start]
            find_ans_helper(letters, i, j, start, used, d_l, ans)
    print('There are ' + str(len(ans)) + ' words in total')


def find_ans_helper(letters, x, y, current_string, used, d_l, ans):
    """
    This function finds the answers of boggle.
    :param letters: list of strings(letters)
    :param x: int, defining which row we are using
    :param y: int, defining which letter we are using
    :param current_string: str, the string we are testing
    :param used: the used location of letters
    :param d_l: the smaller dic based on which letter we starts
    :param ans: list, the answers.
    :return: none
    """
    # Base case
    if 16 >= len(current_string) >= 4 and current_string not in ans and current_string in d_l:
        print('Found: ', current_string)
        # Add the ans to the list
        ans.append(current_string)
    # We don't use else in order to keep looking for words even after we have already found one.
    # Loop over all possible neighboring locations
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i <= 3 and 0 <= y + j <= 3 and [x + i, y + j] not in used:
                # These conditions mean we are looking for all sets of xy between [x-1, x, x+1,], [y-1, y, y+1]
                # Choose
                current_string += letters[x + i][y + j]
                # Recording the used location of letter
                used.append([x + i, y + j])
                # Only Explore when there are words start with current string
                if has_prefix(current_string, d_l):
                    # The current string keep move on to next location
                    find_ans_helper(letters, x + i, y + j, current_string, used, d_l, ans)
                # un - choose
                current_string = current_string[:-1]
                used.pop()


if __name__ == '__main__':
    main()
