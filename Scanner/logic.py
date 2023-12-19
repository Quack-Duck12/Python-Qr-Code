from pyzbar.pyzbar import decode
from PIL import Image

def Qr_Read(path):

    Data = decode(Image.open(path))

    return (str(Data[0][0]).strip("b'"))

def Filesave(Data, Path):
    
    import os

    dir_name = os.path.dirname(Path)
    base_name = os.path.basename(Path)

    file_name = os.path.splitext(base_name)[0]

    new_path = os.path.join(dir_name, file_name + '.txt')

    with open(new_path, 'w') as file:
        file.write(f"Copied From {Path} \n \n {Data}")

