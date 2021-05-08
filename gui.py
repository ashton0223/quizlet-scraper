import sys

from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QLineEdit

class ExampleWindow(QWidget):
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

        test_text = QLabel('test')
        left_layout.addWidget(test_text)

        urlbox = QLineEdit(self)
        left_layout.addWidget(urlbox)

        spreadsheet_button = QPushButton('Get Spreadsheet', self)
        spreadsheet_button.clicked.connect(lambda: self.get_spreadsheet(urlbox.text()))
        spreadsheet_button.resize(spreadsheet_button.sizeHint())
        layout.addWidget(spreadsheet_button)

        self.show()
    
    def get_spreadsheet(self, url):
        print(url)
        self.save_file()
    
    def save_file(self):
        filename = QFileDialog.getSaveFileName(
            self,
            'Save file',
            '',
            'Anki Files (*.apkg);;All Files (*)'
        )

def run():
    app = QApplication(sys.argv)
    ex = ExampleWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()