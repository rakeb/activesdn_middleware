from pyparsing import Word
from string import ascii_lowercase

def myParser():
    uppercase = ascii_lowercase.upper()
    startchar = Word(uppercase, exact=1)
    endchar = Word(ascii_lowercase)
    startword = startchar + endchar
    print(startword.parseString('H'))

if __name__ == '__main__':
    myParser()