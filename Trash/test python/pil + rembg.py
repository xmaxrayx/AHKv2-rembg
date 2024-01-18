
from rembg import remove
from PIL import Image
from PIL import ImageGrab


img = ImageGrab.grabclipboard()

input_path = img
output_path = "C:\\Users\\Max_Laptop\\Desktop\\ssdds.png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)