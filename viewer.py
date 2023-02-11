import tkinter as tk
from PIL import Image, ImageTk
import os, sys

display_time = 2
if(len(sys.argv) == 3):
    display_time = int(sys.argv[2])
elif(len(sys.argv) < 2):
    print("Usage: python viewer.py <absolute-path-to-folder> <display_time>")
    sys.exit()
print(f"\n\nDisplaying images every {display_time} seconds......(default=2s)\n\n")

folder = sys.argv[1]
images = []
window = tk.Tk()
# Create a list to store the images
for img in os.listdir(folder):
    image = Image.open(folder + '/' + img)
    image.thumbnail((800, 600), Image.ANTIALIAS)
    img_obj = ImageTk.PhotoImage(image)
    images.append(img_obj)


# Set the display time for each image
#display_time = 3

# Keep track of the current image index
current_index = 0





# Create a label to display the current image
image_label = tk.Label(window)
image_label.pack()

# Function to display the next image
def display_next_image():
    global current_index
    current_index = (current_index + 1) % len(images)
    image_label.config(image=images[current_index])
    window.after(display_time * 1000, display_next_image)

# Function to delete the current image
def delete_image():
    global images
    global current_index
    del images[current_index]
    current_index = min(current_index, len(images) - 1)
    if len(images) == 0:
        window.destroy()
    else:
        display_next_image()

# Create a button to delete the current image
delete_button = tk.Button(window, text="Delete", command=delete_image)
delete_button.pack()

# Start displaying the images
display_next_image()

# Start the main event loop
window.mainloop()
