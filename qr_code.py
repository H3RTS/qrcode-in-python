import qrcode

qr = qrcode.QRCode( #qrcode format
    border=3,
    box_size=10,
    version=4,
)

qr.add_data('https://youtu.be/jCSvOtUaI8s') #the link we want to convert to qrcode
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="grey") #the colors of the qrcode
img.save('qrcode.png') #we save