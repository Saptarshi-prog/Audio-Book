# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:18:24 2020

@author: 91842
"""
import pyttsx3
import PyPDF2

from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
for num in range(0,pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()

