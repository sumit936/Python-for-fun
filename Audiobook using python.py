"""
This is the code to read pdf file and use python as speaker to read pdf file for us.
"""

import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()#asking for any paf file to choose

#Opening file into read binary mode
book = open(file_path, 'rb')
pdfReader = PyPDF2.PdfFileReader(book)#reading the pdf file
pages = pdfReader.numPages #getting the number of pages
print("The number of pages are: ", pages)#printing the number
speaker = pyttsx3.init() #Initializing the speaker

starting_page = int(input("Enter the starting page(from where you want to start)\nNote: Pages starts from 0:"))
end_page = int(input("Enter the end page: "))

for num in range(starting_page,end_page):
    page = pdfReader.getPage(num)#getting the page which we are about to read
    text = page.extractText()#extracting the text from the page
    speaker.say (text)
    speaker.runAndWait()
