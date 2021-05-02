import quizlet_terms as q
import spreadsheet
import time

input_text = """
What filetype do you want to export to?
1 for .csv (Comma separated)
2 for .txt (Tab separated)
3 for .xls (Excel)
4 for .apkg (Anki package)
5 to quit
"""

def main():
    URL = input('Please enter a quizlet URL:\n--> ')

    #Asks for URL, makes sure it is a good URL
    try:
        page = q.start_session(URL)
        print('got page')
        term_list = q.get_terms(page)
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
                spreadsheet.write_to_csv(term_list)
                break
            elif (filetype == 2):
                spreadsheet.write_to_txt_spreadsheet(term_list)
                break
            elif (filetype == 3):
                spreadsheet.write_to_xls_spreadsheet(term_list)
                break
            elif (filetype == 4):
                spreadsheet.write_to_anki(term_list)
                break
            elif (filetype == 5):
                break
        except:
            print('Invalid input.')

if __name__ == "__main__":
    main()