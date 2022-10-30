import pyqrcode
import png
from pyqrcode import QRCode

s = "9340391241"

cvs = pyqrcode.create(s)

cvs.svg("myqr.svg", scale = 8)

cvs.png('myqr.png', scale = 6)
