import rembg
from rembg import remove

input_path = 'C:\Users\Max_Laptop\Desktop\utau_utane_for_xmaxrayx_by_xmaxrayx_dfeqy7o-pre.jpg'
output_path = 'C:\Users\Max_Laptop\Desktop\utau_utane_for_xmaxrayx_by_xmaxrayx_dfeqy7o-prsssse.jpg'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)



