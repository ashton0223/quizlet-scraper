import sys

from PySide6.QtWidgets import QApplication, QComboBox, QLabel, QWidget, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QLineEdit

from quizlet_sets import sets

class Scraper(QWidget):
    def __init__(self):
        super().__init__()

        self.setup()
    
    def setup(self):
        #self.setGeometry(200, 200,  400, 300)
        self.setWindowTitle('Quizlet Scraper')

        layout = QHBoxLayout()
        layout.setSpacing(20)
        self.setLayout(layout)

        left = QWidget()        
        left_layout = QVBoxLayout()
        left.setLayout(left_layout)
        layout.addWidget(left)

        right = QWidget()
        right_layout = QVBoxLayout()
        right.setLayout(right_layout)
        layout.addWidget(right)

        url_text = QLabel('URL:')
        left_layout.addWidget(url_text)

        self.urlbox = QLineEdit(self)
        left_layout.addWidget(self.urlbox)

        self.add_deck = QWidget()
        add_deck_layout = QVBoxLayout()
        self.add_deck.setLayout(add_deck_layout)
        right_layout.addWidget(self.add_deck)
        self.add_deck.hide()

        add_deck_label = QLabel('Deck name:')
        add_deck_layout.addWidget(add_deck_label)

        self.add_deck_box = QLineEdit(self)
        add_deck_layout.addWidget(self.add_deck_box)

        self.combo = QComboBox()
        self.combo.addItems([
            '.csv (Comma separated)',
            '.txt (Tab separated)',
            '.xls (Excel)',
            '.apkg (Anki package)'
        ])
        self.combo.currentIndexChanged.connect(self.index_changed)
        right_layout.addWidget(self.combo)

        spreadsheet_button = QPushButton('Get Spreadsheet', self)
        spreadsheet_button.clicked.connect(self.get_spreadsheet)
        spreadsheet_button.resize(spreadsheet_button.sizeHint())
        right_layout.addWidget(spreadsheet_button)
    
    def index_changed(self, i):
        self.add_deck.show() if i == 3 else self.add_deck.hide()

    def get_spreadsheet(self):
        try:
            term_list = sets.get_terms(self.urlbox.text())
            self.save_file(term_list)
        except:
            print('Not a valid Quizlet URL.')

    
    def save_file(self, term_list):
        filename = QFileDialog.getSaveFileName(
            self,
            'Save file',
            '',
            'All Files (*)'
        )[0]
        i = self.combo.currentIndex()
        if i == 0:
            term_list.csv(filename + '.csv')
        elif i == 1:
            term_list.txt(filename + '.txt')
        elif i == 2:
            term_list.xls(filename + '.xls')
        elif i == 3:
            term_list.anki(filename + '.apkg', self.add_deck_box.text())
            

def main():
    app = QApplication(sys.argv)
    ex = Scraper()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
