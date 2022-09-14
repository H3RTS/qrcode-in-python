import cv2
#qrcode readers

d = cv2.QRCodeDetector()

qrcode, item, values = d.detectAndDecode(cv2.imread("qrcode.png"))

print(qrcode)