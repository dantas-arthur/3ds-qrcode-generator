import PySimpleGUI as sg
import pyqrcode as pqr
import glob
import png
import io
import os

sg.theme('SystemDefaultForReal')

layout = [[sg.Text('Insira a URL:'), sg.InputText()],
          [sg.Button('Gerar')],
          [sg.Image(key='-IMAGE-')]]

window = sg.Window('3DS QR Generator',
                   layout,
                   size=(500, 400),
                   element_justification='c')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Gerar':

        if values[0] == '':
            sg.popup_error('Digite uma URL válida!')

        else:

            # DELETING OLD QR CODES

            old_files = glob.glob('*.png')
            for filename in old_files:
                os.unlink(filename)

            # URL FILE

            url_data = str(values[0][32:-18])
            final_url = f'https://docs.google.com/uc?export=download&id={url_data}'

            # MAKING A QR CODE:

            qrcode_maker = pqr.create(f'{final_url}')

            with open('qrcode.png', 'w') as fstream:
                qrcode_maker.png('qrcode.png', scale=5)
            qrcode_maker.png('qrcode.png', scale=5)
            buffer = io.BytesIO()
            qrcode_maker.png(buffer)

            # DISPLAYING QR CODE

            window['-IMAGE-'].update(filename='qrcode.png')

window.close()
