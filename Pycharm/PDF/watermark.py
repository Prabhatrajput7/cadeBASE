import PyPDF2
temp = PyPDF2.PdfFileReader(open('super.pdf','rb'))
wmark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
out = PyPDF2.PdfFileWriter()

for i in range(temp.getNumPages()):
    page = temp.getPage(i)
    page.mergePage(wmark.getPage(0))
    out.addPage(page)
    with open('wout.pdf', 'wb') as wout:
        out.write(wout)