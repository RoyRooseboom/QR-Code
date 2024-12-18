import qrcode

img = qrcode.make("Zet hier je tekst neer\nExtra Informatie")
img.save("MaakEenQrCode.jpg")