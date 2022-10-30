import pyqrcode
import png
from pyqrcode import QRCode
import os

s = "https://linktr.ee/durgesh_malviya_"
url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 10)
url.png("myqr.png", scale = 10)
