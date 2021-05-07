import xlwt
from xlwt import Workbook
from classes import term
import csv
import genanki

#Writes a list of terms to a .xls spreadsheet
def write_xls(term_list, name):
    wb = Workbook()

    sheet = wb.add_sheet('Sheet')

    #Write terms and definitions
    x = 1
    for i in term_list:
        sheet.write(x, 0, i.word)
        sheet.write(x, 1, i.definition)
        x += 1

    wb.save(name)

#Writes a list of terms to a .txt tab delimited spreadsheet
def write_txt(term_list, name):
    f = open(name, 'w+')

    #Write terms and definitions
    for i in term_list:
        f.write(i.word + '\t' + i.definition + '\n')
    f.close()

def write_csv(term_list, name):
    with open(name, 'w+', newline='') as file:
        writer = csv.writer(file)
        for i in term_list:
            writer.writerow([i.word, i.definition])

def write_anki(term_list, deck_name, name):
    model = genanki.Model(
        2123350969,
        'Model',
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
        deck_name
    )
    for i in term_list:
        note = genanki.Note(
            model = model,
            fields = [i.word, i.definition]
        )
        deck.add_note(note)
    
    genanki.Package(deck).write_to_file(name)