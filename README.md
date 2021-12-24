# quizlet-scraper
quizlet-scraper is a script that takes a quizlet URL and puts all of the vocabulary words and definitions into a spreadsheet. It is useful for importing vocabulary into programs like Anki or just simply storing the study sets as spreadsheets..

## How to use:
Head to [releases](https://github.com/ashton0223/quizlet-scraper/releases) and download the appropriate zip file for your OS. Afterwards, just unzip and run the program.

## Making an executable:
The releases for quizlet-scraper were created using [PyInstaller](https://www.pyinstaller.org/). To make an executable from the source, install PyInstaller, then run `pyinstaller --onefile -w gui.py` (for the graphical version) or `pyinstaller --onefile scraper.py` (for the command line version) in the project directory.
