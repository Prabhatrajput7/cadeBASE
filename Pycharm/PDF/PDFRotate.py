import PyPDF2
import sys

with open('dummy.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    print(reader.numPages)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('Drotate.pdf','wb') as ro:
        writer.write(ro)