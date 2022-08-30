#imports
from tkinter import *
from translate import Translator

#translate function
def translate():
  translator = Translator(from_lang=lan1.get(), to_lang=lan2.get())
  translation = translator.translate(var.get())
  var1.set(translation)

#Tkinter root window

root = Tk()
root.title('Translator')
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=4)
mainframe.rowconfigure(0, weight=2)
mainframe.pack(pady= 150, padx=150)
root.configure(bg="red")

#variables for drop down list
lan1 = StringVar(root)
lan2 = StringVar(root)

#choices for languages
choices = {"English", "Spanish", "Arabic", "Hindi","French","German"}

#Default selection
lan1.set('English')
lan2.set('Arabic')

#Creating drop down and arranging the grid
#language 1
lan1menu = OptionMenu(mainframe, lan1, *choices)
Label(mainframe, text="Select a language to translate to: ")
lan1menu.grid(row = 1, column = 1)

#language 2
lan2menu = OptionMenu(mainframe, lan2, *choices)
Label(mainframe, text="Select a language to translate into: ")
lan2menu.grid(row = 1, column = 2)

#Text box to take user input
Label(mainframe, text = "Select a language:").grid(row=2,column=0)
var = StringVar()
textbox = Entry(mainframe, textvariable = var).grid(row=2,column=1)

#textbox to show output
Label(mainframe, text = 'Output').grid(row=2,column=2)
var1 = StringVar()
textbox = Entry(mainframe, textvariable = var1).grid(row=2,column=3)

#translator button
b = Button(mainframe, text='Translate',command=translate).grid(row=3,column=1,columnspan = 3)


root.mainloop

















