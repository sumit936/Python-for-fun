"""
This is the code use to encrypt any pdf file.
"""

#Importing relevant packages

from PyPDF2 import PdfFileReader, PdfFileWriter
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()#asking for any paf file to choose
file = file_path.split('/')#extracting the filename from the pdf
file_name = file[-1]
file_name = "Encrypted "+file_name

pdf = PdfFileReader(file_path)#Reading the pdf file
out_pdf = PdfFileWriter()#Creating an instace of pdf file writer

pages = pdf.numPages# getting the number of pages
for i in range(pages):
    page_details = pdf.getPage(i)#extracting the details of each page
    out_pdf.addPage(page_details)#adding the page to out_pdf

password = input("Enter your password for encryption: ")

out_pdf.encrypt(password)#using encrypt method to encrypt the pdf

with open(file_name,'wb') as filename:
    out_pdf.write(filename)

print("\nYou can find your encrypted file under file name 'Encrypted filename(i.e. your original file name)' into your current directory!")