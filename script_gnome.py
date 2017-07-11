import PyPDF2
import pyttsx
from gtts import gTTS
import pdfminer 
import os

clip_location = './clips/'

tts = gTTS(text='Good morning', lang='en')
tts.save(clip_location + "good.mp3")
os.system("mpg123 " + clip_location + "good.mp3")

class CharacterLine:
    words = ""

    def __init__(self, line_number, character):
        self.line_number = line_number
        self.character = character

    def print_line(self):
        return str(self.line_number) + " - " + self.character + ": " + str(self.words)

    def add_words(self, word):
        self.words += " " + word


class Lines:
    dialog = []

    def __init__(self, characters, starting_line_number=0):
        self.characters = characters
        self.line_number = starting_line_number
        self.starting_line_number = starting_line_number

    def extract_lines(self, text):

        for word in text.split():
            # print(word)

            if word in self.characters:
                # print("found!!" + word)
                line = CharacterLine(self.line_number, word)
                self.line_number += 1
                if self.line_number > (self.starting_line_number):
                    # print("adding line to dialog")
                    self.dialog.append(line)

                continue    # to not add character name to the line


            if self.dialog:
                # print("adding word to line")
                line.add_words(word)
            # else:
            #     print("no dialog")

        for ln in self.dialog:
            print(ln.print_line())
                
    def print_dialog(self):
        for lines in dialog:
            print(lines.words)

# ---------------- #

convert('CPF_play_formatting2.pdf')

# script = open('CPF_play_formatting2.pdf', 'rb')
with open('CPF_play_formatting2.pdf', 'rb') as script:
    pdf_script = PyPDF2.PdfFileReader(script)

    characters = ["DONALD", "BLAIRE"]
    script_lines = Lines(characters)

    page_obj = pdf_script.getPage(10)
    page = page_obj.extractText()

    # print(page)
    script_lines.extract_lines(page)


