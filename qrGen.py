import qrcode
import pathlib
import time as t
# User input to 
userChoice = input("What type of QR code do you need? (Link or for a Wifi netowrk?) ").lower()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
while True:
    if userChoice == "link":
        link = input("Enter a valid link. ")
        qr.add_data(link)
        qr.make(fit=True)

        if "https://" not in link:
            print("Invalid link")
            break
        
        img = qr.make_image(fill_color="black", back_color="white")
        save = pathlib.Path.home() / "Downloads"/ "QR Code.png"
        img.save(save)
        print(f"Your QR code was saved in {save}")
        t.sleep(1)
        break
    elif userChoice == "wifi":
        wifiLink1 = input("Enter a valid wifi code ")
        qr.add_data(wifiLink1)
        qr.make(fit=True) 
        
        if "WIFI:" not in wifiLink1:
            print("Invalid Wifi")
            break 
        
        img = qr.make_image(fill_color="black", back_color="white")
        save1= pathlib.Path.home() / "Downloads"/ "QR Code.png"
        img.save(save1)    
        print(f"Your QR code was saved in {save1}")
        t.sleep(1)
        break
    else:
        print("Invalid Response")
        t.sleep(2)
        break 
    