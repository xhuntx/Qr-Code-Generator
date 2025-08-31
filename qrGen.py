import qrcode
import pathlib

userChoice = input("What type of QR code do you need? (Link or for a Wifi netowrk?) ").lower()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
while True:
    if userChoice == "link":
        qr.add_data(input("Please input a valid link. "))
        qr.make(fit=True)
         
        if "https://" not in qr.add_data:
            print("Invalid link")
            break 
        
        img = qr.make_image(fill_color="black", back_color="white")
        save = pathlib.Path.home() / "Downloads"/ "QR Code.png"
        img.save(save)
        print(f"Your QR code was saved in {save}")

    
