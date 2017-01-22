table_file = open("table.txt", "r")
list_file = open("list.txt", "r")

table_frequency_dictionary = { "A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0 }
list_frequency_dictionary = { "A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0 }
    
def full_list_creator(file_name, frequency_dictionary):

    small_list = []
    full_list = []

    for line in file_name:
        line = line.strip("\n")
        small_list.append(line)

    for word in small_list:
        temp_list = []
        for letter in word:
            temp_list.append(letter)
            if (letter == " "):
                pass
            else:
                frequency_dictionary[letter.upper()] += 1
        full_list.append(temp_list)

    return full_list

full_word_list = full_list_creator(list_file, list_frequency_dictionary)
full_table_list = full_list_creator(table_file, table_frequency_dictionary)

frequency_list = sorted(table_frequency_dictionary, key=table_frequency_dictionary.__getitem__)

for frequent_letter in frequency_list:
    for word in full_word_list:
        for letter in word:
            if (letter == frequent_letter):
                #print(letter) # This is the least frequent letter in the first word.
                for letter_line in full_table_list:
                    if letter in letter_line:
                        print(letter)
                        print(letter_line)
        

table_file.close()
list_file.close()
