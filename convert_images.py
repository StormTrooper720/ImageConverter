from tkinter import *
import tkinter as tk
from PIL import Image
from tkinter import filedialog
img = None
text = "Image Converter In Python"


def file_open():
    global img
    filename = filedialog.askopenfilename(initialdir="/", title="Open An Image", filetypes=(
        ("Image Files", "*.png*"), ("Image Files", "*.jpg*"), ("Image Files", "*.jpeg*"), ("Image Files", "*.ico*"),
        ("Image Files", "*.tif*"), ("Image Files", "*.tiff*"), ("Image Files", "*.jp2*"), ("Image Files", "*.bmp*"),
        ("Image Files", "*.gif*")))
    try:
        img = Image.open(fr"{filename}")
    except AttributeError:
        print()
    label_file_explorer.configure(text="File Opened: " + filename)


def file_save():
    global img
    global label_file_explorer
    save_file = filedialog.asksaveasfilename(initialdir="/", title="Save The Image", filetypes=(
        ("Image Files", "*.png*"), ("Image Files", "*.jpg*"), ("Image Files", "*.jpeg*"), ("Image Files", "*.ico*"),
        ("Image Files", "*.tif*"), ("Image Files", "*.tiff*"), ("Image Files", "*.jp2*"), ("Image Files", "*.bmp*")))
    try:
        img.save(save_file)
        label_file_explorer.configure(text="Image Saved As: " + save_file)
    except ValueError:
        label_file_explorer.configure(text="You must add a valid file type at the end of the file's name")
    except OSError:
        label_file_explorer.configure(text="An error has occurred while converting an image to a JPEG/JPG. "
                                           "The JPEG/JPG Format does not support RGBA color format")
    except NameError:
        label_file_explorer.configure(text="You must use a valid image type")
    except KeyError:
        label_file_explorer.configure(text="You must use a valid image type")


window = Tk()
window.title('Image Converter')
window.geometry("707x150")
window.config(background="white")
label_file_explorer = Label(window, text=text, width=100, height=4, fg="blue")

button_open = Button(window, text="Open File", command=file_open)
button_convert = Button(window, text="Convert File", command=file_save)

label_file_explorer.grid(column=1, row=1)
button_open.grid(column=1, row=2)
button_convert.grid(column=1, row=3)
window.mainloop()
