import pyttsx3
import PyPDF2
book = open('Scienceofscience.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
speaker = pyttsx3.init()
speaker.setProperty('rate',140)
for a in range(1,pages):
    eachpage = pdfreader.getPage(a)
    content = eachpage.extractText()
    speaker.say(content)
    speaker.runAndWait()