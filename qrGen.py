import qrcode
import pathlib

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(input("Please input a valid link. "))
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
save = pathlib.Path.home() / "Downloads"/ "QR Code.png"
img.save(save)
print(f"Your QR code was saved in {save}")