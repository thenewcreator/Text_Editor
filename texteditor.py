import sys

v = sys.version
if "2.7" in v:
    from Tkinter import *
    import tkFileDialog

root = Tk("Text Editor")
text = Text(root)
text.grid()


def open_command():
    file = tkFileDialog.askopenfile(parent=root, mode='rb', title='Select a file')
    if file != None:
        contents = file.read()
        t = text.get("1.0", contents)

        file.close()

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = tkFileDialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=saveas)
filemenu.add_separator()

button = Button(root, text="Save", command=saveas)
button.grid()


def FontHelvetica():
    global text

    text.config(font="Helvetica")


def FontCourier():
    global text

    text.config(font="Courier")


font = Menubutton(root, text="Font")
font.grid()
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu
Helvetica = IntVar()
arial = IntVar()
times = IntVar()
Courier = IntVar()
font.menu.add_checkbutton(label="Courier", variable=Courier,
                          command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=Helvetica,
                          command=FontHelvetica)
root.mainloop()

