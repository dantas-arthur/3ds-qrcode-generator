import tkinter
import customtkinter
from PIL import ImageTk, Image
import pyqrcode as pqr
import glob
import png
import os
import io


def qr_generator():

    errormsg.configure(text="")  # Remove old QR codes

    print(textbox.get("0.0", "end"))

    if textbox.get("0.0", "end") == "":  # URL checker
        errormsg.configure(text="Use a valid URL!", fg_color="red")
    elif not (textbox.get("0.0", "end").startswith("https://drive.google.com") or textbox.get("0.0", "end").startswith("https://archive.org")):
        errormsg.configure(text="Use a valid URL!", fg_color="red")
    else:
        old_files = glob.glob("*.png")  # Deleting old QR codes
        for filename in old_files:
            os.unlink(filename)

        if "https://drive.google.com" in textbox.get("0.0", "end"):
            url = textbox.get("0.0", "end")[32:-18]
            edited_url = f"https://docs.google.com/uc?export=download&id={url}"
        else:
            edited_url = textbox.get("0.0", "end")

        qr_code = pqr.create(edited_url)  # QR code generator
        qr_code.png("qrcode.png", scale=5)

        with open('qrcode.png', 'w') as fstream:
            qr_code.png('qrcode.png', scale=5)
        qr_code.png('qrcode.png', scale=5)
        buffer = io.BytesIO()
        qr_code.png(buffer)

        qrc = customtkinter.CTkImage(light_image=Image.open("qrcode.png"), size=(250, 250))  # Display QR code
        qrlabel.configure(qrframe, text="", image=qrc)
        qrlabel.pack()


root = customtkinter.CTk() # CustomTK Window

root.title("3DS QR Codes")
root.iconbitmap("assets/icon.ico")
root.geometry("500x650")
root.resizable(width=False, height=False)

appTitle = customtkinter.CTkLabel(
    root, 
    text="3DS QR CODES", 
    font=("Segoe UI Black", 35), 
    text_color="#208097"
    )
appTitle.pack(pady=5)

absolute_path = os.path.dirname(__file__)
relative_path = '../assets/icone-grande.png'
image_path = os.path.join(absolute_path, relative_path)
image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path)), size=(150, 150))
label = customtkinter.CTkLabel(root, text="", image=image)
label.pack(pady=10)

frame = customtkinter.CTkFrame(root) # URL field
textbox = customtkinter.CTkTextbox(frame, width=350, height=20) 
textbox.pack(pady=25)
paste = customtkinter.CTkButton(
    frame, 
    text="Paste", 
    width=65, 
    height=30, 
    fg_color="#208097"
    )
textbox.grid(row=0, column=0)
paste.grid(row=0, column=1, padx=10)
frame.pack()

errormsg = customtkinter.CTkLabel(root, text="") # Error mensage
qrframe = customtkinter.CTkFrame(root, width=250, height=250)
qrlabel = customtkinter.CTkLabel(qrframe, text="", image="")
qrframe.pack(pady=25)

button = customtkinter.CTkButton(
    root, 
    text="Start", 
    font=("TkHeadingFont", 35), 
    width=180, height=75, 
    corner_radius=5, 
    fg_color="#208097",
    command=qr_generator
    )
button.place(relx=0.5, rely=0.92, anchor=tkinter.CENTER)

root.mainloop()
