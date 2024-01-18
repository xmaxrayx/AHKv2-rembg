# from PIL import ImageGrab
# import io
# import codecs

# # Pull image from clibpoard
# img = ImageGrab.grabclipboard()

# # Get raw bytes
# img_bytes = io.BytesIO()
# img.save(img_bytes, format='PNG')

# # Convert bytes to base64
# base64_data = codecs.encode(img_bytes.getvalue(), 'base64')

# # Convert base64 data to a string
# base64_text = codecs.decode(base64_data, 'ascii')

# # Create an HTML img tag with data embedded
# html_img_tag = "<img src="data:image/png;base64, %s" />" % base64_text

# # Print HTML tag to console (might be long).
# # You can put this img tag in to HTML and the browser
# # will render the image.
# print(html_img_tag)












from PIL import ImageGrab
import pathlib

#outputLocation =  r'C:\Users\Max_Laptop\Desktop\saa.png'

desktop = pathlib.Path.home() / 'Desktop' 
outputLocation = str(desktop) + "\\dsss.png"


image = ImageGrab.grabclipboard()




image.save(outputLocation, 'PNG')



