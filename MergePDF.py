import PyPDF2

# Open the files that have to be merged one by one
pdf1File = open('1.pdf', 'rb')
pdf2File = open('2.pdf', 'rb')
pdf3File = open('3.pdf', 'rb')

# Read the files that you have opened
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdf3Reader = PyPDF2.PdfFileReader(pdf3File)

# Create a new PdfFileWriter object which represents a blank PDF document
pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the pagenumbers for the first document
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# Loop through all the pagenumbers for the second document
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# Loop through all the pagenumbers for the third document
for pageNum in range(pdf3Reader.numPages):
    pageObj = pdf3Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
# Now that you have copied all the pages in both the documents, write them into the a new document
pdfOutputFile = open('MergedFiles.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

# Close all the files - Created as well as opened
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()
pdf3File.close()