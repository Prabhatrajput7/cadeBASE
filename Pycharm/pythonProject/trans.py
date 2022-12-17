import sys
from translate import Translator

translator= Translator(to_lang="en")
try:
    with open('tesx.txt',mode='r') as myfile:
        txt = myfile.read()
        translation = translator.translate(txt)
        with open('out.text', mode='w') as myfile2:
            myfile2.write(translation)
except FileNotFoundError as err:
    print('File is not there BROOO')
    raise err