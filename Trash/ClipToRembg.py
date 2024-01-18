from email.mime import image
import io
from h11 import Data
from rembg import remove
from PIL import Image
from PIL import ImageGrab




input_image = clipboard_image = ImageGrab.grabclipboard().tobytes() # get the image from the clipboard





output_path = "C:\\Users\\Max_Laptop\\Desktop\\output.png" # specify the output file name

bytes_io = io.BytesIO(input_image.convert("RGBA")) # convert the image to bytes

output = remove(input_image) # remove the background from the input image
output_image = Image.open(bytes_io).convert("RGBA") # convert the output byte array to an image
#io.BytesIO(output).write(open("output.png", "wb")



output_image.save(output_path) # save the output image