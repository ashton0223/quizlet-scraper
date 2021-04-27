# quizlet-scraper
Script that takes a quizlet URL and puts all of the vocabulary words and definitions into a spreadsheet. Useful for importing vocabulary into programs like Anki.

## How to use:
Head to [releases](https://github.com/ashton0223/quizlet-scraper/releases) and download the appropriate binaries for your OS. Then, just run the program. It will ask you for a quizlet URL, what you want to name the file, and what type of spreadsheet you want.

## Making an executable:
The releases for quizlet-scraper were created using [PyInstaller](https://www.pyinstaller.org/). To make an executable from the source, install PyInstaller, then run `pyinstaller --onefile scraper.py` in the project directory.
