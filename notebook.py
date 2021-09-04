from tkinter import *
from tkinter import filedialog

def zoom():
   scale = Scale(master=window,from_=0,to=2000,length=100,font=(2),orient=HORIZONTAL)
   scale.pack()
   text.config(font=(int(scale.get())))

def saveAs():
    file = filedialog.asksaveasfile(
                                    initialdir='C:\\Users\\user\\Desktop',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('text file','.txt'),
                                        ('html file','.html'),
                                        ('all file','.*')
                                    ]
                                    )

    fileText=str(text.get(1.0,END))
    file.write(fileText)

def open():
    filepath = filedialog.askopenfilenames(
                                    initialdir='C:\\Users\\user\\Desktop',
                                    )

    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()

menubar = Menu(
               master=window
              )
window.config(menu=menubar,width=1000,height=460)

fileMenu = Menu(master=menubar,tearoff=0)
editMenu = Menu(master=menubar,tearoff=0)
formatMenu = Menu(master=menubar,tearoff=0)
viewMenu = Menu(master=menubar,tearoff=0)
helpMenu = Menu(master=menubar,tearoff=0)

menubar.add_cascade(label="File",menu=fileMenu)

fileMenu.add_command(label="New     Ctrl+N")
fileMenu.add_command(label="New Window   Shift+Ctrl+N")
fileMenu.add_command(label="Open...   Ctrl+O",command=open)
fileMenu.add_command(label="Save      Ctrl+S")
fileMenu.add_command(label="Save As   Ctrl+Shift+S",command=saveAs)
fileMenu.add_separator()
fileMenu.add_command(label="Page Setup...")
fileMenu.add_command(label="Print...   Ctrl+P")
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

menubar.add_cascade(label="Edit",menu=editMenu)

editMenu.add_command(label="Undo      Ctrl+N")
editMenu.add_separator()
editMenu.add_command(label="Cut   Shift+Ctrl+X")
editMenu.add_command(label="Copy     Ctrl+C")
editMenu.add_command(label="Paste     Ctrl+V")
editMenu.add_command(label="Delete    Del")


menubar.add_cascade(label="Format",menu=formatMenu)

formatMenu.add_command(label="World Wrap")
formatMenu.add_command(label="Font....")

menubar.add_cascade(label="View",menu=viewMenu)

viewMenu.add_command(label="Zoom    >")
viewMenu.add_command(label="Status Bar")

menubar.add_cascade(label="Help",menu=helpMenu)

helpMenu.add_command(label="View Help")
helpMenu.add_command(label="Send Feedback")
helpMenu.add_separator()
helpMenu.add_command(label="About Notpad")


text = Text(
            master=window,

           )
text.pack(expand=True,fill='both')

window.mainloop()