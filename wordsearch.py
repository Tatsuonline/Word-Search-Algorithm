# This algorithm quickly and efficiently solves word search puzzles.
# It first finds the frequency of each of letter in the puzzle,
# then it takes each word from the word list and picks a letter
# in the word with the lowest frequency. It then checks all the
# letters around that letter to find another matching letter.

import sys

word_list = open("list.txt", "r")
table = open("table.txt", "r")
letter_list = []
frequency_list = []
table_matrix = []
new_list = []
letter_frequency_list = []
new_letter_list = []
lowest_frequency_letter_index = 0
lowest_frequency = 0
lowest_frequency_letter = "NONE" # Random, doesn't matter.
previous_letters = []
next_letters = []
row_counter = 0
count_down = 0

for line in table:
    for letter in line:
        if letter == "\n" or letter == " ":
            continue
        if letter not in letter_list:
            letter_list.append(letter)
            frequency_list.append(1)
        else:
            frequency_list[letter_list.index(letter)] = frequency_list[letter_list.index(letter)] + 1
        new_list.append(letter)
    table_matrix.append(new_list)
    new_list = []

for word in word_list:
    for word_letter in word:
        if word_letter == "\n":
            continue
        else:
            letter_frequency_list.append(frequency_list[letter_list.index(word_letter)])
            new_letter_list.append(word_letter)
    lowest_frequency = min(letter_frequency_list)
    lowest_frequency_letter_index = letter_frequency_list.index(lowest_frequency)
    lowest_frequency_letter = new_letter_list[lowest_frequency_letter_index]
    if lowest_frequency_letter_index != 0 and lowest_frequency_letter_index != len(new_letter_list) - 1:
        previous_letters = new_letter_list[0:lowest_frequency_letter_index]
        next_letters = new_letter_list[lowest_frequency_letter_index + 1: len(new_letter_list)]
    elif lowest_frequency_letter_index == 0 and lowest_frequency_letter_index != len(new_letter_list) - 1:
        next_letters = new_letter_list[lowest_frequency_letter_index + 1: len(new_letter_list)]
    elif lowest_frequency_letter_index != 0 and lowest_frequency_letter_index == len(new_letter_list) - 1:
        previous_letters = new_letter_list[0:lowest_frequency_letter_index]
    else:
        print "Error: You can't search for a word that is only one letter long!"
    # Do a search in table matrix for lowest freq letter and check if previous letters are around it.
    # If so, check if next letters are around it.
    # If so, place all letters in the found word in parenthesis to indicate found.
    for table in table_matrix:
        for table_letter in table:
            if table_letter == lowest_frequency_letter:
                if row_counter != 0 and table.index(table_letter) != 0: # [0][0] stuff!
                    count_down = len(previous_letters)
                    for i in reversed(previous_letters):
                        if i == table_matrix[row_counter - 1][table.index(table_letter) - 1]: # NW
                            pass
                        elif i == table_matrix[row_counter - 1][table.index(table_letter)]: # N
                            pass
                        elif i == table_matrix[row_counter - 1][table.index(table_letter) + 1]: # NE
                            pass
                        elif i == table_matrix[row_counter][table.index(table_letter) + 1]: # E
                            pass
                        elif i == table_matrix[row_counter + 1][table.index(table_letter) + 1]: # SE
                            pass
                        elif i == table_matrix[row_counter + 1][table.index(table_letter)]: # S
                            pass
                        elif i == table_matrix[row_counter + 1][table.index(table_letter) - 1]: # SW
                            pass
                        elif i == table_matrix[row_counter][table.index(table_letter) - 1]: # W
                            pass
                        else:
                            break
                elif row_counter == 0 and table.index(table_letter) != 0:
                    pass
                elif row_counter != 0 and table.index(table_letter) == 0:
                    pass
                else:
                    pass
        row_counter += 1
    letter_frequency_list = []
    new_letter_list = []
    previous_letters = []
    next_letters = []
    row_counter = 0
