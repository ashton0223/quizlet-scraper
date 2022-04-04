from quizlet_sets import sets

import time
from os import path

input_text = """
What filetype do you want to export to?
1 for .csv (Comma separated)
2 for .txt (Tab separated)
3 for .xls (Excel)
4 for .apkg (Anki package)
5 to quit
"""

#Asks for filename and returns it. Also checks if it exists
def get_filename(filetype):
    filename = input('Filename: ')
    check_file(filename + filetype)
    return filename + filetype

def get_deck_name():
    return input('Deck name: ')

#Checks if file exists, if it does not, throw exception
def check_file(filename):
    if(path.exists(filename)):
        print('File already exists')
        raise Exception("File already exists")


def main():
    url = input('Please enter a quizlet URL:\n--> ')

    #Asks for URL, makes sure it is a good URL
    try:
        term_list = sets.get_terms(url)
    except:
        print('Not a valid Quizlet URL.')
        time.sleep(2)
        quit()

    #Repeatedly asks for selection until a valid one is given,
    #then creates a file of that selection
    while True:
        try:
            filetype = int(input(input_text))
            if (filetype < 1 or filetype > 5):
                raise Exception('Invalid selection')
            elif (filetype == 1):
                name = get_filename('.csv')
                term_list.csv(name)
                break
            elif (filetype == 2):
                name = get_filename('.txt')
                term_list.txt(name)
                break
            elif (filetype == 3):
                name = get_filename('.xls')
                term_list.xls(name)
                break
            elif (filetype == 4):
                deck_name = get_deck_name()
                name = get_filename('.apkg')
                term_list.anki(deck_name, name)
                break
            elif (filetype == 5):
                break
        except:
            print('Invalid input.')

if __name__ == "__main__":
    main()