import qrcode

url = "https://francesca-effe.github.io/lr9-ar/video.html"

img = qrcode.make(url)
img.save("lr9-qr.png")

print("QR code saved as lr9-qr.png")