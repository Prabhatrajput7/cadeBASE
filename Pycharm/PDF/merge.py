import PyPDF2
import sys

inp = sys.argv[1:]

def pdf_combine(p_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in p_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combine(inp)