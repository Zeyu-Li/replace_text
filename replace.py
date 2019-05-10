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


def main():
    """ Takes string and replaces it with values in dictionary """

    string = """Once upon a time a Wolf was lapping at a spring on a hillside,
when, looking up, what should he see but a Lamb just
beginning to drink a little lower down. ‘There’s my supper,’
thought he, ‘if only I can find some excuse to seize it.’ Then
he called out to the Lamb, ‘How dare you muddle the water
from which I am drinking?’
‘Nay, master, nay,’ said Lambikin; ‘if the water be muddy
up there, I cannot be the cause of it, for it runs down from
you to me.’
‘Well, then,’ said the Wolf, ‘why did you call me bad
names this time last year?’
‘That cannot be,’ said the Lamb; ‘I am only six months
old.’"""

    # opens json dictionary
    try:
        with open('replace.json', 'r') as fp:
            dictionary = json.load(fp)

        index = 0
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
            index += 1

            # new line break every 9 words
            if index % 10 == 9:
                print("")

    except:
        fail = True

    if not fail:
        print("The translation was successful")
    else:
        print("Failed to translation because json was not given")

    return 0

# system calls name
if __name__ == "__main__":
    main()
