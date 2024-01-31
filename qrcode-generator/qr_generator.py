import tkinter
import customtkinter
from PIL import Image
from pathlib import Path
import pyqrcode as pqr
import glob
import png
import sys, os
import io


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def qr_generator():

    qrlabel.configure(text="")  # Remove old QR codes
    qrlabel.pack()

    if textbox.get("0.0", "end") == "":  # URL checker
        qrlabel.configure(text="Use a valid URL!", text_color="red")
        qrlabel.pack()
    elif not (textbox.get("0.0", "end").startswith("https://drive.google.com") or textbox.get("0.0", "end").startswith("https://archive.org")):
        qrlabel.configure(text="Use a valid URL!", text_color="red")
        qrlabel.pack()
    else:
        old_files = glob.glob("*.png")  # Deleting old QR codes
        for filename in old_files:
            os.unlink(filename)

        if "https://drive.google.com" in textbox.get("0.0", "end"):
            url = textbox.get("0.0", "end")[32:-18]
            edited_url = f"https://drive.google.com/uc?export=download&id={url}"
        else:
            edited_url = textbox.get("0.0", "end")

        qr_code = pqr.create(edited_url)  # QR code generator
        qr_code.png("qrcode.png", scale=5)

        with open('qrcode.png', 'w') as fstream:
            qr_code.png('qrcode.png', scale=5)
        qr_code.png('qrcode.png', scale=5)
        buffer = io.BytesIO()
        qr_code.png(buffer)

        qrc = customtkinter.CTkImage(light_image=Image.open("qrcode.png"), size=(275, 275))  # Display QR code
        qrlabel.configure(qrframe, text="", image=qrc)
        qrlabel.pack()


root = customtkinter.CTk() # CustomTK Window

root.title("3DS QR Code")
root.iconbitmap(resource_path("assets/icon.ico"))
root.geometry("500x600")
root.resizable(width=False, height=False)

appTitle = customtkinter.CTkLabel(
    root, 
    text="3DS QR CODES", 
    font=("Segoe UI Black", 35), 
    text_color="#208097"
    )
appTitle.pack(pady=5)

image = customtkinter.CTkImage(light_image=Image.open(resource_path("assets/icone-grande.png")), size=(150, 150))
label = customtkinter.CTkLabel(root, text="", image=image)
label.pack(pady=10)

frame = customtkinter.CTkFrame(root, fg_color="transparent") # URL field
textbox = customtkinter.CTkTextbox(frame, width=350, height=20) 
textbox.pack(pady=25)
paste = customtkinter.CTkButton(
    frame, 
    text="Create", 
    width=65, 
    height=30, 
    fg_color="#208097",
    command=qr_generator
    )
textbox.grid(row=0, column=0)
paste.grid(row=0, column=1, padx=10)
frame.pack()

errormsg = customtkinter.CTkLabel(root, text="") # Error mensage
qrframe = customtkinter.CTkFrame(root, width=275, height=275, fg_color="transparent")
qrlabel = customtkinter.CTkLabel(qrframe, text="", image="")
qrframe.pack(pady=25)

root.mainloop()
