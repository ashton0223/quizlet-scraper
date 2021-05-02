import os.path
from os import path
import xlwt
from xlwt import Workbook
from classes import term
import csv
import genanki

#Writes a list of terms to a .xls spreadsheet
def write_to_xls_spreadsheet(term_list):
    filename = get_filename('.xls')

    wb = Workbook()

    sheet = wb.add_sheet('Sheet')

    #Write terms and definitions
    x = 1
    for i in term_list:
        sheet.write(x, 0, i.word)
        sheet.write(x, 1, i.definition)
        x += 1

    wb.save(filename)

#Writes a list of terms to a .txt tab delimited spreadsheet
def write_to_txt_spreadsheet(term_list):
    filename = get_filename('.txt')
    f = open(filename, 'w+')

    #Write terms and definitions
    for i in term_list:
        f.write(i.word + '\t' + i.definition + '\n')
    f.close()

def write_to_csv(term_list):
    filename = get_filename('.csv')
    with open(filename, 'w+', newline='') as file:
        writer = csv.writer(file)
        for i in term_list:
            writer.writerow([i.word, i.definition])

def write_to_anki(term_list):
    model = genanki.Model(
        2123350969,
        fields = [
            {'name' : 'Question'},
            {'name' : 'Answer'}
        ],
        templates = [
            {
                'name' : 'Card 1',
                'qfmt' : '{{Question}}',
                'afmt' : '{{FrontSide}}<hr id="answer">{{Answer}}'
            }
        ]
    )
    deck = genanki.Deck(
        1164622816,
        get_deck_name()
    )
    for i in term_list:
        note = genanki.Note(
            model = model,
            fields = [i.word, i.definition]
        )
        deck.add_note(note)
    
    genanki.Package(deck).write_to_file(get_filename('.apkg'))

    
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
