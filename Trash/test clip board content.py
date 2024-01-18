from PIL import Image, ImageGrab

# copy an image to the clipboard
# for example, by using the Print Screen key on Windows

# get the clipboard image
clipboard_image = ImageGrab.grabclipboard()
import ctypes  # An included library with Python install.   



# check the type of the returned value
if isinstance(clipboard_image, Image.Image):
    # it is an image object, you can use it directly
    ctypes.windll.user32.MessageBoxW(0, "clip", "Your title", 1)

    clipboard_image.show()
elif isinstance(clipboard_image, list):
    # it is a list of filenames, you can open them with Image.open()
    for filename in clipboard_image:
        ctypes.windll.user32.MessageBoxW(0, "file", "Your title", 1)
        image = Image.open(filename)
        image.show()
        
else:
    # it is None, the clipboard does not contain image data or filenames
    print("No image data found in the clipboard")
