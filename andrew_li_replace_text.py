""" Replace Text

Course: CS 30
Period: 3
Date created: May 10, 2019
Date completed: May 14, 2019
By: Andrew Li
This program replaces words in a string object with words in a dictionary

"""

# import modules
import json
import re


# string that is going to be replaced
def replace(string, dictionary):
    """ replaces a string with what is supplied in the dictionary """

    #  splits the string into all components including special characters
    split = re.split('(\W)', string)
    new_paragraph = []

    for word in split:

        # if in dictionary, replace
        if word.lower() in dictionary:
            # special case for I
            if word == "I":
                word = "We"
            elif word not in dictionary:
                word = dictionary[word.lower()].title()
            else:
                word = dictionary[word.lower()]

        new_paragraph.append(word)

    # once finished, write to output file and print
    with open('new_text.txt', 'w') as fp:
        fp.write("".join(new_paragraph))
    print("".join(new_paragraph))


def main():
    """ Takes string and replaces it with values in dictionary """

    flag = False
    # opens and reads text that needs to be modified
    try:
        with open('old_text.txt', 'r') as fp:
            string = fp.read()

    # if file not found, report error to user
    except FileNotFoundError:
        print("The text that is to be modified does not exist")
        flag = True

    # finds and opens json dictionary
    try:
        if flag:
            raise MyException("MissingOldText")
        with open('replace.json', 'r') as fp:
            dictionary = json.load(fp)
        replace(string, dictionary)
        print("The translation was successful")
    except FileNotFoundError:
        print("Failed to translation because json was not given")
    except MyException:
        pass

    return 0

# system calls name
if __name__ == "__main__":
    main()
