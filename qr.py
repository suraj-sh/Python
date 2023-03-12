# Generating a normal QRCode 
import qrcode as qr
img = qr.make("https://github.com/suraj-sh")
img.save("suraj_github.png")

# Generating QRCode with styling like border & color
import qrcode 
from PIL import Image

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.ERROR_CORRECT_H,
                    box_size=10, border=4)
qr.add_data("https://www.linkedin.com/in/surajmhsharma/")
# qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="white")
img.save("suraj_linkedin.png")
