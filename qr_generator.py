import qrcode


github_url = "https://github.com/carlos-fuentes15"


qr = qrcode.make(github_url)


qr.save("github_qr.png")

print("QR Code generated and saved as github_qr.png")
