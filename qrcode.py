import pyqrcode as qr
from pyqrcode import QRCode

s = "https://github.com/mani3523" # your url here

# To generate QR code 
url = qr.create(s) 

# Create and save the png file naming "myqr.png" 
url.svg("mygithub.svg", scale = 8)