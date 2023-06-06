import pyqrcode as pqr
import png
import io
import glob
import os

while True:
    # DELETING OLD QR:

    old_files = glob.glob('*.png')
    for filename in old_files:
        os.unlink(filename)

    # URL DATA:

    print('\033[1m-\033[m'*45)
    url_data = str(input('URL: ')[32:-18])
    final_url = f'https://docs.google.com/uc?export=download&id={url_data}'
    print('\033[1m-\033[m'*45)

    # MAKING A QR CODE:

    qrcode_maker = pqr.create(f'{final_url}')

    with open('qrcode.png', 'w') as fstream:
        qrcode_maker.png('qrcode.png', scale=5)
    qrcode_maker.png('qrcode.png', scale=5)
    buffer = io.BytesIO()
    qrcode_maker.png(buffer)

    # FINAL:

    print(f'\033[1;32m{"QR Code criado com sucesso!":^45}\033[m')
    print('\033[1m-\033[m'*45)
    break
