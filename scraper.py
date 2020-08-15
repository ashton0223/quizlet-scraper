import quizlet_terms as q
import spreadsheet

def main():
    URL = input('Please enter a quizlet URL:\n')

    #Asks for URL, makes sure it is a good URL
    try:
        page = q.start_session(URL)
        term_list = q.get_terms(page)
    except:
        print('Not a valid Quizlet URL.\n')
        quit()

    #Repeatedly asks for selection until a valid one is given,
    #then creates a file of that selection
    while True:
        try:
            filetype = int(input('What filetype do you want to export to?\n1 for .txt (Reccomended for Anki)\n2 for .xls\n3 to quit\n'))
            if (filetype < 1 or filetype > 3):
                raise Exception('Invalid selection')
            if (filetype == 1):
                spreadsheet.write_to_txt_spreadsheet(term_list)
                break
            if (filetype == 2):
                spreadsheet.write_to_xls_spreadsheet(term_list)
                break
            if (filetype == 3):
                break
        except:
            print('Invalid input.')

if __name__ == "__main__":
    main()