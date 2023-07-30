from tkinter import *
import os

def btn_clicked():
    global entry0
    b='cmd /k python Server.py '
    string=entry0.get()
    b=b+string
    os.system(b)

def withwrawwindow():
    window.withdraw()

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

background_img = PhotoImage(file = f"server_gui/background.png")
background = canvas.create_image(
    250.0, 250.0,
    image=background_img)

img0 = PhotoImage(file = f"server_gui/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: [withwrawwindow(),btn_clicked()],
    relief = "flat")

b0.place(
    x = 135, y = 335,
    width = 231,
    height = 32)

entry0_img = PhotoImage(file = f"server_gui/img_textBox0.png")
entry0_bg = canvas.create_image(
    267.5, 276.5,
    image = entry0_img)


entry0 = Entry(
    bd = 0,
    bg = "#d1d1d1",
    highlightthickness = 0)

entry0.place(
    x = 175, y = 261,
    width = 185,
    height = 29)

window.resizable(False, False)
window.mainloop()
