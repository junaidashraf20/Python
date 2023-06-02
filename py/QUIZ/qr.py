import qrcode
img = qrcode.make(
    'https://www.youtube.com/'

)
img.save('myQRcode.png')
img.show()