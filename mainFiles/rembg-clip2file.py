#!defVEnv python

##C:\Users\Max_Laptop\Programming\Github\xMaxrayx_Github\leaning-Python-\pythonProject\myenv
# from rembg import remove

# input_path = 'input.png'
# output_path = 'output.png'

# with open(input_path, 'rb') as i:
#     with open(output_path, 'wb') as o:
#         input = i.read()
#         output = remove(input)
#         o.write(output)
from cgi import test
import io
from rembg import remove
from PIL import ImageGrab
import win32clipboard
from PIL import Image
import pyperclip
from io import BytesIO
import ctypes
import pythoncom
import win32clipboard
from ctypes import wintypes


def send_to_clipboard_noalpha(image):
    
   

    output = BytesIO()
    image.convert("RGBA").save(output, "PNG")
    

    data = output.getvalue()[14:]   
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    output.close()
    win32clipboard.CloseClipboard()


from PIL import Image
import io
import win32clipboard

def send_transparent_to_clipboard(image):
    output = io.BytesIO()
    image.save(output, format='PNG')
    data = output.getvalue()
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()



def send_to_clipboard(image):
    output = io.BytesIO()
    image.convert('RGB').save(output, 'BMB')
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()




def ahkToRembg(operationType="clip2clip" , modelType=""):   
    if operationType == "clip2file":
        img = ImageGrab.grabclipboard()
        output = remove(img)
        output.save('output.png', 'PNG')
    elif operationType == "clip2clip":
        img = ImageGrab.grabclipboard()
        output = remove(img)
        print(type(output))
        output_bytes = output.tobytes()
        print(type(output_bytes))
        send_to_clipboard_noalpha(output)
        # send_transparent_to_clipboard(output)
    elif  operationType == "clip2file2clip":
        img = ImageGrab.grabclipboard()
        output = remove(img)
        output.save('output.png', 'PNG')
        #img_nobg = Image.open(output)        
        # Create an in-memory stream to hold the image data
        img_nobg_stream = io.BytesIO()
        output.save(img_nobg_stream, format='PNG')
        img_nobg_stream.seek(0)
        
        # Copy the image data to the clipboard
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, img_nobg_stream.read())
        win32clipboard.CloseClipboard()
    elif operationType == "clip2clipv2":
        # img = ImageGrab.grabclipboard()
        # output = remove(img)
        # output.save('output.png', 'PNG')
       
       
        output = BytesIO()
        img = ImageGrab.grabclipboard()
        output = remove(img)
        final = output
        final.save("output.png", "PNG")
        data = final.getvalue()
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.RegisterClipboardFormat('PNG'),data)
        win32clipboard.CloseClipboard()
    elif operationType== test_resultDidNotWork:
        class DROPFILES(ctypes.Structure):
            _fields_ = [("pFiles", wintypes.DWORD),
                        ("pt", wintypes.POINT),
                        ("fNC", wintypes.BOOL),
                        ("fWide", wintypes.BOOL)]

        path = "C:\\Users\\Max_Laptop\\Desktop\\utau_utane_for_xmaxrayx_by_xmaxrayx_dfeqy7o-prsssse.png"

        offset = ctypes.sizeof(DROPFILES)
        size = offset + (len(path) + 1) * ctypes.sizeof(ctypes.c_wchar) + 1
        buffer = (ctypes.c_char * size)()
        df = DROPFILES.from_buffer(buffer)
        df.pFiles = offset
        df.fWide = True

        wchars = (ctypes.c_wchar * (len(path) + 1)).from_buffer(buffer, offset)
        wchars.value = path

        stg = pythoncom.STGMEDIUM()
        stg.set(pythoncom.TYMED_HGLOBAL, buffer)

        win32clipboard.OpenClipboard()

        try:
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_HDROP, stg.data)
        finally:
            win32clipboard.CloseClipboard()


#ahkToRembg("clip2file")
ahkToRembg("test")
#ahkToRembg("clip2clipv2")

# img = ImageGrab.grabclipboard()


# # Store the bytes in a byte stream
# img_bytes = io.BytesIO()
# #img.save(img_bytes, format='PNG')

# print(img_bytes.getvalue())


# output = remove(img)

# output.save('output.png', 'PNG')


# #print(output.getvalue())





    
def send_to_clipboard2(image,clip_type):
    
    

    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()



