import pyttsx3

import PyPDF2
book = open('Scienceofscience.pdf','rb')
pdfr = PyPDF2.PdfFileReader(book)
pages = pdfr.numPages
speaker = pyttsx3.init()
for p in range(1,pages):
    eachpage = pdfr.getPage(p)
    text=eachpage.extractText()
    speaker.say(text)
    speaker.runAndWait()