#!C:\usrbin\python.exe 

##C:\Users\Max_Laptop\Programming\Github\xMaxrayx_Github\leaning-Python-\pythonProject\myenv
# from rembg import remove

# input_path = 'input.png'
# output_path = 'output.png'

# with open(input_path, 'rb') as i:
#     with open(output_path, 'wb') as o:
#         input = i.read()
#         output = remove(input)
#         o.write(output)
import io
from rembg import remove
from PIL import ImageGrab


img = ImageGrab.grabclipboard()


# Store the bytes in a byte stream
img_bytes = io.BytesIO()
#img.save(img_bytes, format='PNG')

print(img_bytes.getvalue())


output = remove(img)

output.save('output.png', 'PNG')
