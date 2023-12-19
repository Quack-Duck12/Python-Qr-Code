import qrcode
from random import choice,randint
from pyzbar.pyzbar import decode
from PIL import Image

import pycountry

import os

if not os.path.exists("TestImage"):
    os.makedirs("TestImage")


Test_Num = int(input("Enter Number Of Test Images: "))+1

def Generate_QR(data, ver, bord, colour,name,locate):
    qr = qrcode.QRCode(
        version=ver,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=bord,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='#000000', back_color=colour)

    img.save(r"{}{}".format(locate,name))

def Qr_Read(path):

    Data = decode(Image.open(path))

    value = str(Data[0][0]).strip("b'")

    print(value)


Country = [country.name for country in pycountry.countries]

colour = ['white','gray','yellow','green','red','blue','cyan','gold','silver','purple','pink','orange','brown']


print("Generating Qr-Code\n")
for i in range(Test_Num):

    Generate_QR(choice(Country),randint(1,40),randint(0,50),choice(colour),f"Test_{i}.png","TestImage\\")
    print(f"Number_{i} Done")
    print()

print("Scanning Qr-Code\n")
for i in range(Test_Num):
    print(f"Test_{i}")
    Qr_Read(f"TestImage\Test_{i}.png")
    print()

