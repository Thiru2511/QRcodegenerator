import qrcode
import image
qr=qrcode.QRCode(
    version=15,#high the no big the code image
    box_size=10,#size of the box
    border=5 #outer
)
data="https://thiruparker2511.neocities.org/foody/"

qr.add_data(data)
qr.make(fit=True)

img=qr.make_image(fill="black",back_color="white")
img.save("foody.png")