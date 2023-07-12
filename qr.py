# Generation of QR code

import qrcode

# URL to be opened when QR code is scanned
image = qrcode.make("https://127.0.0.1:8000")
image.save("qr.png")