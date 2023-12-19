import qrcode

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