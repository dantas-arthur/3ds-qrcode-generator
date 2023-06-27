<h1 align='center'>3DS QR Code Generator</h1>
<p align='center'>A simple QR code generator for installing games on FBI</p>

<div align="center">
  <img src="./assets/icone-grande.png" alt="icone-grande">
</div>

<h2 align="center">ℹ️ IMPORTANT ℹ️</h2>

<p align="center">
  This project has the sole purpose of helping the Nintendo 3DS community and assisting me in the learning process of new programming languages. I do not endorse piracy in any way. When using any resources provided in this repository, make sure to <strong>dump</strong> a copy of your original game.
</p>

## Purpose:

The purpose of this repository is to make the process of installing games on the Nintendo 3DS a bit easier. As you may already know, when we install a game by moving files to the internal storage of the 3DS, it costs twice the internal memory (the space consumed by the ```.cia``` file and the space needed to install the game). Even if you select the option to delete the ```.cia``` file after installation, personally speaking, it is quite inconvenient to have to delete a file that I would like to keep. Considering these issues, I decided to create a simple script that generates a QR code so that I can install a game in a much more convenient way. "But why use Google Drive?" Simply to keep the files secure in a cloud service, and I can also save the memory of my devices.

## How to use:

#### Cloning the repository
Before we begin, clone the repository to have local access to all the necessary files. You can do this using the following command:

```
git clone https://github.com/LonelyALpHaz/3ds-qrcode-generator.git
```

#### Generating the QR code
1. Upload the game you want to install to [Google Drive](https://www.google.com/intl/pt-br/drive/about.html), make sure to **dump** original games in this process and use only games in the ```.cia``` format, otherwise FBI won't be able to install the game.
2. Make the file accessible to the public by going to ```Share > Anyone with the link``` and copy the file link.
3. Run the ```qr_code.py``` script available in this repository, paste the copied link into the "URL" field, and then click the "Generate" button. Wait a few seconds and the QR code will appear in the program interface.

#### Installing the game on the 3DS
1. Open the FBI application on your Nintendo 3DS, and on the first screen, select the options ```Remote Install > Scan QR Code```.
2. Point the camera of your 3DS to the previously generated QR code and, on the bottom screen, click "Yes" to allow the download via QR code.
3. Wait while the game is being installed, and at the end of the process, click "OK" to finish the installation.
4. When you return to the home screen of the console, it will display the classic screen with a gift. Simply open it and enjoy your new game.

## Resources used:

This project utilized the ```Python``` programming language, version 3.11.1, the ```pypng``` and ```pyqrcode``` modules were used to generate the QR code, and the ```Tkinter``` module was used to create the graphical interface.

## Disclaimer:

I am a junior programmer, so if any errors are found in the script or if you have suggestions on how I can improve the project, feel free to open an issue!
