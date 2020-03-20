import pyqrcode
import os

wd = os.getcwd()
os.chdir(wd + "//")


def qr_gen(string, filename):
    qr = pyqrcode.create(string)
    img = qr.png(wd + "//"+filename)

    return img
