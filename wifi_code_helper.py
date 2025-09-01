wifiName = input("Enter Wifi name as shown in your settings ")
security = input("If you are using a modern network it is WPA if not it is WEP Enter none if your wifi has no password ")
password = input("Enter your password (I will not have this info it is saved localy) enter none if you don't have a passoword ")

if security and password == "none":
    print(f"Your wifi code is: \nWIFI:S:{wifiName};T:nopass;;")
else:
    print(f"Your wifi code is: \nWIFI:S:{wifiName};T:{security};P:{password};;")