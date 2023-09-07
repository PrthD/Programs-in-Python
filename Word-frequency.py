import sys


def command_line_process():
    """ Processes the command given in the terminal to run the program and
        checks for the proper way and arguments used to run the program.

        Arguments: no arguments needed to run the function.

        Returns:
            filename: The name of the text file passed in the terminal command
                      that will be used in the program.
    """
    # error handling for whether the number of input command arguments passed
    # in the terminal to run the program are appropriate or not and returning
    # the filename if appropriate arguments are passed
    if len(sys.argv) < 2:
        exit('Too few arguments. Usage: python3 freq.py <input file name>')
    elif len(sys.argv) > 2:
        exit('Too many arguments. Usage: python3 freq.py <input file name>')
    filename = sys.argv[1]
    return(filename)


def open_file(in_file_name):
    """ Opens the files for reading and writing from which the input will be
        read and written respectively. It also ensures the name of both the
        files is same except for the extension ('.out') of writing file.

        Arguments:
                in_file_name: the name of the input text file (returned by the
                          function command_line_process) from which input
                          will be read.

        Returns:
            fin: file object for the input text file opened for reading.
            fout: file object for the file opened for writing the output.
    """
    # opening files for reading and writing and returning their file objects
    fin = open(in_file_name, "r")
    # concatenating the extension '.out' to the name of input text file
    # and creating the name of the file for writing
    out_file_name = in_file_name + '.out'
    fout = open(out_file_name, "w")
    return(fin, fout)


def input_file_read(fin):
    """ Reads the input text file and gathers each word of each line of the
        text file into a list called input_list.

        Arguments:
            fin: file object (returned by function open_file) for the input
                 text file opened for reading.

        Returns:
            input_list: the list containing all the words of every line of
                        the input text file.
    """
    # reading all lines of the input text file, splitting them into
    # words, collecting and returning them in a list
    input_list = []
    for line in fin:
        list = line.strip().split()
        input_list.extend(list)
    return(input_list)


def inp_list_process(input_list):
    """ Creates a dictionary which contains all different words, from the
        list input_list, as the keys and the frequency of their occurence
        in input_list as its value.

        Arguments:
            input_list: the list containing all the words of every line of
                        the input text file.

        Returns:
            word_count_dict: the dictionary containing all different words
                             from the input text file as the keys and their
                             frequency of occurence as their values.
    """
    # creating a dictionary with words of the input text file as keys
    # and their frequancy of appearance in the input text file as
    # their values
    word_count_dict = {}
    for word in input_list:
        word_count_dict[word] = input_list.count(word)
    return(word_count_dict)


def write_output_file(fout, input_list, word_count_dict):
    """ Writes all different words, the number of times they appear in the
        input text file, and their frequency in a tabular form in the output
        file that was opened for writing by the function open_file.

        Arguments:
            fout: file object for the file opened for writing the output.
            input_list: the list containing all the words of every line of
                        the input text file.
            word_count_dict: the dictionary containing all different words
                             from the input text file as the keys and their
                             frequency of occurence as their values.
        Returns: this function just writes to a file and returns nothing.
    """
    # writing the word, the number of times it appears in the input text
    # file and its frequency for every different word in input text file
    # to a file
    for key, value in sorted(word_count_dict.items()):
        # frequency = (number of times a word apears in a text)
        #              /(total number of words in the text)
        freq = round(value/len(input_list), 3)
        fout.write(key + ' ' + str(value) + ' ' + str(freq) + '\n')

filename = command_line_process()
fin, fout = open_file(filename)
input_list = input_file_read(fin)
fin.close()
final_dict = inp_list_process(input_list)
write_output_file(fout, input_list, final_dict)
fout.close()

