from PIL import ImageGrab, Image
import io



img = ImageGrab.grabclipboard()


print(img)

str(img)
img_bytes = io.BytesIO()




import rembg
from rembg import remove

input_path = img_bytes #TypeError: expected str, bytes or os.PathLike object, not NoneType
output_path = "C:\\Users\\Max_Laptop\\Desktop"

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

