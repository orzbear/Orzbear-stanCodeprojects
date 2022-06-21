"""
File: babynames.py
Name: 
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    if name not in name_data:
        # If the name is not in the name_data yet, creating the key and enter its info(year and rank)
        name_data[name] = {year: rank}
    elif year not in name_data[name]:
        # If the name is in the name_data, but the specific year is not in the dic, create and entering the info.
        name_data[name][year] = rank
    elif year in name_data[name] and int(rank) < int(name_data[name][year]):
        # If the rank of a specific name in the specific year exist, but the input rank is higher, replace it.
        name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    d = {}  # Empty dic to save the info
    with open(filename, 'r') as f:  # Opening the file according to the filename
        year = 0  # Empty int to store the year of each file
        for line in f:
            names = []  # Empty list ot store the names
            tokens = line.split(',')  # Split the text with commons
            for token in tokens:
                token = token.strip()  # Deleting the space and /n in the text
                names.append(token)  # add them into the list
            if len(tokens) == 1:  # Identifying the year str in the file
                year = line.strip()  # Deleting the space and /n in the text
            else:
                # Storing the info in the dic
                # The format will be{Name: {year: rank}}
                if names[1] not in d:
                    # If the name has not been saved in the dic, create one
                    d[names[1]] = {year: names[0]}
                if names[2] not in d:
                    # If the name has not been saved in the dic, create one
                    d[names[2]] = {year: names[0]}
                # There's no need to replace the old one with the new one since we are only keeping the higher one, and
                # the higher one always comes the first
    for name in d:
        for year in d[name]:
            # Adding the data to the name_data using milestone 1
            rank = d[name][year]
            add_data_for_name(name_data, year, rank, name)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for filename in filenames:
        # Read files from filenames and add data into the dic name_data
        add_file(name_data, filename)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    matching_names = []
    for name in name_data:
        #  If the target string is in a name from out dic name_data, saveit to matching_names.
        if target.lower() in name.lower():  # it should be case-insensitive
            matching_names.append(name)
    return matching_names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
