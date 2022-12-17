import PyPDF2
import sys

with open('OD223277697133230000.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(1)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('OD223277697133230000pdf.pdf','wb') as ro:
        writer.write(ro)