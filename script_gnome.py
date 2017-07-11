import PyPDF2
from gtts import gTTS
import os

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO, BytesIO
# from cStringIO import StringIO


# clip_location = './clips/'

# tts = gTTS(text='Good morning', lang='en')
# tts.save(clip_location + "good.mp3")
# os.system("mpg123 " + clip_location + "good.mp3")

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

# script = open('CPF_play_formatting2.pdf', 'rb')
# with open('CPF_play_formatting2.pdf', 'rb') as script:
#     pdf_script = PyPDF2.PdfFileReader(script)

#     characters = ["DONALD", "BLAIRE"]
#     script_lines = Lines(characters)

#     page_obj = pdf_script.getPage(10)
#     page = page_obj.extractText()

#     # print(page)
#     script_lines.extract_lines(page)

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    print(pagenos)
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    st = retstr.getvalue()
    retstr.close()

    f = open('workfile', 'w')
    f.write(st)
    return st


if __name__ == "__main__":
    #scrape = open("../warandpeace/chapter1.pdf", 'rb') # for local files
    # scrape = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf") # for external files
    pdfFile = convert_pdf_to_txt('CPF_play_formatting2.pdf')

    print(pdfFile)
