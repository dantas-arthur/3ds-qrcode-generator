import tkinter as tk
from PIL import ImageTk
import pyqrcode as pqr
import glob
import png
import os
import io

def qr_generator():

    # Removing Old QR

    label_qrcode.config(image='')
    
    # URL Check
    
    if txtinput.get() == '' or 'https://drive.google.com' not in txtinput.get():
        label_qrcode.config(text='Use a valid URL!', fg='red')

    else:
        # DELETING OLD QR CODES

        old_files = glob.glob('*.png')
        for filename in old_files:
            os.unlink(filename)

        # URL FILE

        url = txtinput.get()[32:-18]
        final_url = f'https://docs.google.com/uc?export=download&id={url}'

        # MAKING A QR CODE:

        qrcode_maker = pqr.create(f'{final_url}')

        with open('qrcode.png', 'w') as fstream:
            qrcode_maker.png('qrcode.png', scale=5)
        qrcode_maker.png('qrcode.png', scale=5)
        buffer = io.BytesIO()
        qrcode_maker.png(buffer)

        # DISPLAYING QR CODE

        qrc = ImageTk.PhotoImage(file='qrcode.png')

        label_qrcode.config(image=qrc)
        label_qrcode.image = qrc

# TK Initiallizer

root = tk.Tk()
root.title('3DS QR Generator')
root.eval('tk::PlaceWindow . center')

frame1 = tk.Frame(root, width=500, height=630, bg='#0e6475')
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

# Title Label

tk.Label(
    frame1, 
    text='3DS QR Code Generator',
    bg='#0e6475',
    fg='white',
    font=('Microsoft Sans Serif', 20),
    pady=15
).pack()

# Logo Image

logo_img = ImageTk.PhotoImage(file='assets/icone-pequeno.png')
logo_widget = tk.Label(frame1, image=logo_img, bg='#0e6475')
logo_widget.pack()

# Text Input URL

txtinput = tk.Entry(frame1, width=55)
txtinput.pack()

# QR Code Display Frame

qrcode_frame = tk.Frame(frame1, bg='#0e6475', pady=10)
qrcode_frame.pack()

# QR Code Display Image

label_qrcode = tk.Label(qrcode_frame, bg='#0e6475', font=('Default', 12))
label_qrcode.pack()

# Generate QR Button

button_frame = tk.Frame(frame1, bg='#0e6475')
button_frame.pack(side=tk.BOTTOM, pady=5)

generate_button = tk.Button(
    button_frame,
    text='Generate',
    font=('TkHeadingFont', 20),
    bg='#0e6475',
    fg='white',
    width=10,
    pady=10,
    cursor='hand2',
    activebackground='#badee2',
    activeforeground='black',
    command=lambda:qr_generator()
)
generate_button.pack()

root.mainloop()
