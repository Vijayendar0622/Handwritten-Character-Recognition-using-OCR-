import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from tkinter import PhotoImage
import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
top = tk.Tk()
top.geometry('1920x1080')
top.title('HAND WRITTING TO TEXT')
top.iconphoto(True, PhotoImage(file="logo_w.png"))
img = ImageTk.PhotoImage(Image.open("logo_w.png"))

label = Label(top, text="HandWritten Character Regonistion ", bg="#353935", fg="#FFFFFF", font=('Times', 25))
label.pack()

im1 = Image.open("logo_w.png")
ima = im1.resize((330, 260))
img = ImageTk.PhotoImage(ima)

top.configure(background='#FFFFFF')
label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))

label1 = tk.Label(image=img)
label1.image = ima
label1.place(x=600, y=70)

label.pack()
ran = Image.open("Upload2.jpg")
ran = ran.resize((300, 200))
up = ImageTk.PhotoImage(ran)

sign_image = Label(top, image=up)
plate_image = Label(top, bd=10)

State1 = Label(top, text="", bg="#353935", foreground='#FFFFFF', font=('Times', 24))


def classify(file_path):
    img = Image.open(file_path)
    text = tess.image_to_string(img)

    print(text)

    label.configure(foreground='#FFFFFF', text=text, bg="#353935")

    plate_image.place(x=100, y=100)


def show_classify_button(file_path):
    classify_b = Button(top, text="Get Text", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#3734eb', foreground='white', font=('arial', 15, 'bold'))
    classify_b.place(x=500, y=650)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)

        uploaded.thumbnail(((top.winfo_width() / 5), (top.winfo_height() / 5)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')

        State1.configure(text='')
        show_classify_button(file_path)
    except:
        pass
upload = Button(top, text="Upload image", command=upload_image, padx=10, pady=15)
upload.configure(background='#3734eb', foreground='white', font=('arial', 9, 'bold'))
upload.pack()
upload.place(x=210, y=650)
sign_image.pack()
sign_image.place(x=150, y=400)
label.pack()
label.place(x=940, y=250)
State1.pack()
State1.place(x=925, y=500)
top.mainloop()