import requests
from bs4 import BeautifulSoup
from classes import term

#Starts HTML session and returns result of get_page
def start_session(URL):
    user_agent = {'User-agent': 'Mozilla/5.0'} # Security triggered otherwise
    return requests.get(URL, headers=user_agent)

#Gets terms from HTML and puts them into a list of terms
def get_terms(page):
    term_list = []
    soup = BeautifulSoup(page.text, 'html.parser')

    #Gets list of terms from HTML, but not text directly 
    terms = soup.findAll('div', {'class': 'SetPageTerm-content'})
    #Gets each term from the list of terms, and gets the text for each term and definition
    #Then puts it in the term list
    for i in terms:
        #Gets term, removes any tabs
        a = i.find('a', {'class': 'SetPageTerm-wordText'})
        if('    ' in a.text):
            a.text.replace('    ', '     ')
            print('Tab found in terms. This has been replaced with 5 spaces so that a tab-delimited spreadsheet can be created.\n')

        #Gets definition, removes any tabs
        b = i.find('a', {'class': 'SetPageTerm-definitionText'})
        if('    ' in b.text):
            b.text.replace('    ', '     ')
            print('Tab found in definitions. This has been replaced with 5 spaces so that a tab-delimited spreadsheet can be created.\n')

        current_term = term(a.text, b.text)

        term_list.append(current_term)

    if(len(term_list) == 0):
        raise Exception('Invalid URL')

    return term_list
