from PyPDF2 import PdfFileWriter, PdfFileReader
print('test')
pages_to_delete = [0] # page numbering starts from 0
infile = PdfFileReader('2.File.pdf', 'rb')
output = PdfFileWriter()

for i in range(infile.getNumPages()):
    if i not in pages_to_delete:
        p = infile.getPage(i)
        output.addPage(p)

with open('newfile.pdf', 'wb') as f:
    output.write(f)