""" Replace Text

Course: CS 30
Period: 3
Date created: May 10, 2019
Date completed: May 10, 2019
By: Andrew Li
This program replaces words in a string object with words in a dictionary

"""

# import modules
import json


# string that is going to be replaced

def replace(string, dictionary):

    # for words in the text, split by line break or space
    for word in string.replace("\n", " ").split(" "):

        # if it is in the dictionary, change the word
        # to the one in the dictionary
        if word.lower() in dictionary:
            if word not in dictionary and word != "I":
                word = dictionary[word.lower()].title()
            else:
                word = dictionary[word.lower()]

        print(word, end=' ')

        # new line break every 9 words


def main():
    """ Takes string and replaces it with values in dictionary """

    # opens json dictionary
    try:
        with open('old_text.txt', 'r') as fp:
            string = fp.read()
    except FileNotFoundError:
        print("The text that is to be modified does not exist")
    try:
        with open('replace.json', 'r') as fp:
            dictionary = json.load(fp)
        replace(string, dictionary)
        print("The translation was successful")
    except FileNotFoundError:
        print("Failed to translation because json was not given")

    return 0

# system calls name
if __name__ == "__main__":
    main()
