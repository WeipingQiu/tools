from pdf2image import convert_from_path
from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)

def convert_pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path, poppler_path=r"C:\Users\eweiqiu\Documents\Software\poppler\Release-21.10.0-0\poppler-21.10.0\Library\bin")
    for index, image in enumerate(images):
        image.save(f'{pdf_path}-{index}.png')


convert_pdf_to_images('Vaccination.pdf')
