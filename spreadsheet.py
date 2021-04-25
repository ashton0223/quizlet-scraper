import os.path
from os import path
import xlwt
from xlwt import Workbook
from classes import term
import csv

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
    
#Asks for filename and returns it. Also checks if it exists
def get_filename(filetype):
    filename = input('Spreadsheet name: ')
    check_file(filename + filetype)
    return filename + filetype

#Checks if file exists, if it does not, throw exception
def check_file(filename):
    if(path.exists(filename)):
        print('File already exists')
        raise Exception("File already exists")
