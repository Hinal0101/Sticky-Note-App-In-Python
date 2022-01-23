from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import random
import datetime as dt
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


root = Tk()
root.title("Sticky Notes")
root.geometry("500x500")
count_number=0
current_window = root

font = "Book Antiqua"
size = 16
def btn_plus():
    global textBox, size

    size+=1
    new_font = Font(family=font, size=size, weight="normal")
    try:
        textBox.selection_get()
        textBox.tag_add("new font", "sel.first", "sel.last")
        textBox.tag_config("new font", font=new_font)
    except TclError:
        textBox.configure(font=new_font)
    label_3 = Label(current_window, text=size, borderwidth=3, font=("helvetica", 15))
    label_3.place(in_=heading_enter, x=135, anchor=N)

def btn_minus():
    global textBox, size

    size -= 1
    new_font = Font(family=font, size=size, weight="normal")
    try:
        textBox.selection_get()
        textBox.tag_add("new font", "sel.first", "sel.last")
        textBox.tag_config("new font", font=new_font)
    except TclError:
        textBox.configure(font=new_font)
    heading_size = Label(current_window, text=size, borderwidth=3, font=("helvetica", 15))
    heading_size.place(in_=heading_enter, x=135, anchor=N)


def size_box():
    label_2 = Label(current_window, text="Font size ", borderwidth=3, font=("helvetica", 15), width=500)
    label_2.place(in_=heading_enter, x=53, anchor=N)

    button_plus = Button(current_window, text="+", command=btn_plus)
    button_plus.place(in_=heading_enter, x=155, anchor=N)
    button_minus = Button(current_window, text="-", command=btn_minus, width=2)
    button_minus.place(in_=heading_enter, x=105, anchor=N)

    current_window.update()


def disable_event():

   global count_number
   if count_number:
        response = messagebox.askyesnocancel("Exit Window", "Are you sure you want to discard the note?",icon='question')
        print(response)
        if response == None:
            pass
        elif response:
            print(array, " inside disable event")
            array.pop().destroy()
            print("done success")
        else:
            save_file()
   else:
       current_window.destroy()
current_window.protocol("WM_DELETE_WINDOW", disable_event)

array = []
window_num = 1
def new():
    global textBox, open, note, my_frame, count_number, current_window, array, window_num,heading_enter
    if count_number == 0:
        current_window = root
    else:
        current_window = Toplevel(current_window)
        current_window.geometry("500x500")
    current_window.title("Sticky Notes -" + str(window_num))
    print(current_window)
    array.append(current_window)
    print(array)
    heading_enter = Label(current_window, text="Enter the Text Below ", borderwidth=3, font=("helvetica", 15))
    heading_enter.pack()

    heading_date = Label(current_window, text=f"{dt.datetime.now():%a, %b %d %Y}", fg="black", font=("helvetica", 15))
    heading_date.pack()

    my_font = Font(family=font, size=size, weight="normal")

    colors = (
    "#000", "#FAEBD7", "#00FFFF", "#F0FFFF", "#FFE4C4", "#7FFFD4", "#D2691E", "#7FFF00", "#6495ED", "#B8860B",
    "#2F4F4F",
    "#E9967A")
    Scroll = Scrollbar(current_window)
    Scroll.pack(side=RIGHT, fill=Y)

    my_frame = Frame(current_window)
    my_frame.pack()

    text_color = "#000"
    col = random.choice(colors)
    if col == "#000" or col == "#2F4F4F":
        text_color = "#fff"

    textBox = Text(my_frame, font=my_font, bg=col, fg=text_color, width= 200, height=40, undo=True)
    note = textBox.get("1.0", "end-1c")
    textBox.grid(row=2, column=2, columnspan=3)

    Scroll.config(command=textBox.yview)
    textBox.config(yscrollcommand=Scroll.set)
    create_menubar(current_window)
    current_window.protocol("WM_DELETE_WINDOW", disable_event)
    count_number+=1
    window_num+=1

def create_menubar(obj):
    MenuBar = Menu(obj)
    File_menu = Menu(MenuBar, tearoff=0)
    File_menu.add_command(label="New", command=new)
    File_menu.add_command(label="Open", command=open_file)
    File_menu.add_command(label="Save", command=save_file)
    MenuBar.add_cascade(label="File", menu=File_menu)

    Edit = Menu(MenuBar, tearoff=0)
    Edit.add_command(label="Cut", command=Cut)
    Edit.add_command(label="Copy", command=Copy)
    Edit.add_command(label="Paste", command=Paste)
    Edit.add_command(label="Delete", command=clear)
    MenuBar.add_cascade(label="Edit", menu=Edit)

    Format = Menu(MenuBar, tearoff=0)
    Format.add_command(label="Bold", command=Bold_text)
    Format.add_command(label="Italic", command=Italic)
    MenuBar.add_cascade(label="Format", menu=Format)

    Font_Format = Menu(MenuBar, tearoff=0)
    submenu1 = Menu(Font_Format, tearoff=0)
    submenu1.add_command(label="Agency FB", command=lambda: font_change("Agency FB"))
    submenu1.add_command(label="Algerian", command=lambda: font_change("Algerian"))
    submenu1.add_command(label="Arial", command=lambda: font_change("Arial"))
    submenu1.add_command(label="Blackadder ITC", command=lambda: font_change("Blackadder ITC"))
    submenu1.add_command(label="Bauhaus 93", command=lambda: font_change("Bauhaus 93"))
    submenu1.add_command(label="Script MT", command=lambda: font_change("Script MT"))
    submenu1.add_command(label="Pristina", command=lambda: font_change("Pristina"))
    submenu1.add_command(label="Segoe Print", command=lambda: font_change("Segoe Print"))
    submenu1.add_command(label="Palace Script MT", command=lambda: font_change("Palace Script MT"))
    submenu1.add_command(label="Segoe Script", command=lambda: font_change("Segoe Script"))
    submenu1.add_command(label="Times New Roman", command=lambda: font_change("Times New Roman"))
    submenu1.add_command(label="Vivaldi", command=lambda: font_change("Vivaldi"))
    submenu1.add_command(label="Vladimir Script", command=lambda: font_change("Vladimir Script"))
    submenu1.add_command(label="Book Antiqua", command=lambda: font_change("Book Antiqua"))
    submenu1.add_command(label="Calibri", command=lambda: font_change("Calibri"))

    Font_Format.add_cascade(label="Change the Font", menu=submenu1)
    Font_Format.add_command(label="Change the Font size", command=size_box)
    MenuBar.add_cascade(label="Font", menu=Font_Format)
    obj.config(menu=MenuBar)


def clear():
    global textBox, button_new, button_delete, note, count
    count=0
    response=messagebox.askquestion("Delete","Are you sure you want to delete")
    if response=="yes":
        note = textBox.get("1.0", "end-1c")
        textBox.delete("1.0", "end")


def Cut():
    global textBox
    textBox.event_generate(("<<Cut>>"))


def Copy():
    global textBox
    textBox.event_generate(("<<Copy>>"))


def Paste():
    global textBox
    textBox.event_generate(("<<Paste>>"))


def Bold_text():
    global textBox
    bold_font=Font(textBox, textBox.cget("font"))
    bold_font.configure(weight="bold")
    textBox.tag_config("bold", font=bold_font)
    current_tags=textBox.tag_names("sel.first")

    if "bold" in current_tags:
        textBox.tag_remove("bold", "sel.first", "sel.last")
    else:
        textBox.tag_add("bold", "sel.first", "sel.last")


def Italic():
    global textBox
    italic_font = Font(textBox, textBox.cget("font"))
    italic_font.configure(slant="italic")
    textBox.tag_config("italic", font=italic_font)
    current_tags = textBox.tag_names("sel.first")

    if "italic" in current_tags:
        textBox.tag_remove("italic", "sel.first", "sel.last")
    else:
        textBox.tag_add("italic", "sel.first", "sel.last")


def font_change(f):
    global textBox, font, first, last, string
    string =""
    first =0
    last = 0
    font=f
    print(f,size)
    new_font = Font(family=f, size=size, weight="normal")
    try:
        textBox.tag_remove("new font", "sel.first", "sel.last")
        textBox.selection_get()
        textBox.tag_add("new font", "sel.first", "sel.last")
        textBox.tag_config("new font", font=new_font)

        ''' string = textBox.get(tkinter.SEL_FIRST,tkinter.SEL_LAST)
        first= org_str.index(string)
        last = first + len(string)
        textBox.tag_add("new font", first,last)
        textBox.tag_config("new font", font=new_font)'''

    except TclError:
        textBox.configure(font=new_font)
        print("error in font")


file = None


def open_file():
    global file, note, textBox,temp_font

    file = askopenfilename(defaultextension=".txt",filetypes=[("All files","."),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        current_window.title(os.path.basename(file)+ " - Sticky note")
        textBox.delete(1.0, END)
        f = open(file, "r")
        textBox.insert("1.0", f.read())
        temp_font = textBox.get("2.0","2.end")
        temp_size = textBox.get("3.0","3.end")
        print(temp_font)
        textBox.delete("2.0", "3.end")
        new_font = Font(family=temp_font, size=temp_size, weight="normal")
        textBox.configure(font=new_font)

        f.close()


def save_file():
    global file, textBox
    if file == None:
        file = asksaveasfilename(initialdir="Untitled.txt",filetypes=[("All files","."),("Text Documents",".txt"),("PDF Files",".pdf")])

        if file == "":
            file = None
        else:
            f = open(file, "w")
            var = textBox.get("1.0", "end-1c")
            f.write(dt.datetime.now().strftime("%a, %m/%d/%Y"))
            f.write("\n")
            f.write(font)
            f.write("\n")
            f.write(str(size))
            f.write("\n")
            f.write(var)
            f.close()
            current_window.title(os.path.basename(file)+" - Sticky note")
            print("file saved")
    else:
        f = open(file,"w")
        f.write(textBox.get("1.0", "end-1c"))
        f.close()


create_menubar(current_window)
if current_window == root:
    root.mainloop()
else:
    current_window.mainloop()