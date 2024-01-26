"""File Preparation

This script allows the user to prepare a source file into a decision table (dictionary).

This tool accepts text files (.txt).

This file can also be imported as a module and contains the following
functions:

    * open_file - returns the file representation in the "read" mode
    * read_file - returns read file in a string form
    * split_file - returns split file in a string list form
    * read_data - returns data separated by a divider in a list form
"""


def open_file():
    try:
        file_name = input("File name: ")
        if file_name.__contains__(".txt"):
            return open(file_name, "r")
        else:
            return open(file_name + ".txt", "r")
    except FileNotFoundError:
        print("Error: File Not Found")
        return open_file()


def read_file(file) -> str:
    return file.read()


def split_file(split) -> list:
    return split.split()


def read_data(file):
    data = []
    divider = ","
    for element in file:
        data.append(element.split(divider))
    return data


def prepare_file() -> dict:
    decision_dictionary = {}
    data = read_data(split_file(read_file(open_file())))
    attributes = [[row[i] for row in data] for i in range(len(data[0]))]
    for i in range(len(attributes)-1):
        decision_dictionary["a" + f"{i+1}"] = attributes[i]
    decision_dictionary["d"] = attributes[-1]
    return decision_dictionary
