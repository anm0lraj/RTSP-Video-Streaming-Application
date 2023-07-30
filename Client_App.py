from tkinter import *
import os
import time


def btn_clicked():
    global entry0
    d='cmd /k python ClientLauncher.py '
    string=entry0.get()
    d=d+string+' '
    string=entry1.get()
    d=d+string+' '
    string=entry2.get()
    d=d+string+' '
    string=entry3.get()
    d=d+string
    os.system(d)


def withwrawwindow():
    window.withdraw()

def minimise():
    window.iconify()

def openstat():

    def dest():
        stat.destroy()

    def ret():
        window.deiconify()

    stat=Toplevel(window)
    stat.title("Statistics")
    stat.geometry("500x500")
    stat.configure(bg = "#ffffff")
    canvas = Canvas(
        stat,
        bg = "#ffffff",
        height = 500,
        width = 500,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"client_gui/background1.png")
    background = canvas.create_image(
        250.0, 250.0,
        image=background_img)
    back = PhotoImage(file = f"client_gui/back.png")
    btn1 = Button(stat,
        image = back,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:[ret(),dest()],
        relief = "flat")

    btn1.place(
        x = 150, y = 361,
        width = 195,
        height = 27)
    text_file=open("stats.txt",'r')
    f=text_file.read()
    Label(stat,text= f,font=("poppins",10) ,fg="#140D28",bg="#ffffff").pack(pady=200)
    text_file.close()
    stat.resizable(False, False)
    stat.mainloop()


window = Tk()

window.geometry("500x500")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 500,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"client_gui/background.png")
background = canvas.create_image(
    250.0, 250.0,
    image=background_img)

img0 = PhotoImage(file = f"client_gui/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:[withwrawwindow(),btn_clicked()],
    relief = "flat")

b0.place(
    x = 148, y = 409,
    width = 195,
    height = 27)

entry0_img = PhotoImage(file = f"client_gui/img_textBox0.png")
entry0_bg = canvas.create_image(
    262.0, 192.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d1d1d1",
    highlightthickness = 0)

entry0.place(
    x = 184, y = 181,
    width = 156,
    height = 21)

entry1_img = PhotoImage(file = f"client_gui/img_textBox1.png")
entry1_bg = canvas.create_image(
    262.0, 254.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d1d1d1",
    highlightthickness = 0)

entry1.place(
    x = 184, y = 242,
    width = 156,
    height = 23)

entry2_img = PhotoImage(file = f"client_gui/img_textBox2.png")
entry2_bg = canvas.create_image(
    262.0, 315.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#d1d1d1",
    highlightthickness = 0)

entry2.place(
    x = 184, y = 304,
    width = 156,
    height = 21)

entry3_img = PhotoImage(file = f"client_gui/img_textBox3.png")
entry3_bg = canvas.create_image(
    262.0, 377.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#d1d1d1",
    highlightthickness = 0)

entry3.place(
    x = 184, y = 365,
    width = 156,
    height = 23)

img1 = PhotoImage(file = f"client_gui/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:[minimise(),openstat()],
    relief = "flat")

b1.place(
    x = 449, y = 459,
    width = 27,
    height = 26)

window.resizable(False, False)
window.mainloop()
