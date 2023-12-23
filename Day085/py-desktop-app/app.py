import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


# Define pil_img_with_watermark as a global variable
pil_img_with_watermark = None



#TEXT WATERMARK->
#insert text watermark into image and return it
def insert_text_watermark(pil_img, watermark_txt):
    drawing = ImageDraw.Draw(pil_img)
    width, height = pil_img.size
    fill_color = (203, 201, 201)
    font = ImageFont.truetype("KingsmanDemo-1GVgg.ttf", 50)
    x = width / 2 - 50
    y = height / 2 - 50
    position = (x, y)
    drawing.text(position, watermark_txt, font=font, fill=fill_color)
    return pil_img



#upload original image with watermark text that has to be inserted in that image
def upload_file(watermark_txt):
    global pil_img_with_watermark  
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    pil_img = Image.open(filename)
    pil_img_resized = pil_img.resize((400, 400))
    pil_img_with_watermark = insert_text_watermark(pil_img_resized, watermark_txt)

    # Create a Canvas widget and display the watermarked image
    canvas.delete("all")  # Clear existing drawings
    tk_img = ImageTk.PhotoImage(pil_img_with_watermark)
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
    canvas.image = tk_img  # Keep a reference to the image to prevent it from being garbage collected

    # Enable the download button to allow downloading
    download_button.config(state=tk.NORMAL)



#download watermarked image(will first be disabled,then will be enabled only after user has uploaded image)
def download_image():
    global pil_img_with_watermark  # Access the global variable
    if pil_img_with_watermark:
        # Save the watermarked image to a file
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("Jpg Files", "*.jpg")])
        if file_path:
            pil_img_with_watermark.save(file_path)




#take user input for the watermark text.
def input_watermark_txt():
    # Function to get watermark text from user
    def submit_watermark():
        watermark_text = entry.get()
        watermark_window.destroy()  # Close the input window
        upload_file(watermark_text)  # Call upload_file with the entered watermark text

    # Create the watermark window
    watermark_window = tk.Tk()
    watermark_window.title("Watermark Input")

    # Create a Label widget for instructions
    instruction_label = tk.Label(watermark_window, text="Input watermark text:")
    instruction_label.pack(pady=10)
    
    # Create an Entry widget for user input
    entry = tk.Entry(watermark_window)
    entry.pack(pady=10)

    # Create a button to submit the watermark text
    submit_button = tk.Button(watermark_window, text="Submit", command=submit_watermark)
    submit_button.pack(pady=10)

    # Start the Tkinter loop for just watermark window
    watermark_window.mainloop()






####IMAGE WATERMARK ->
def insert_img_watermark(watermark_img_resized):
    global pil_img_with_watermark
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types, title="Select an Image watermark or Logo")
    pil_img = Image.open(filename)
    pil_img_resized = pil_img.resize((400, 400))
    x=0
    y=0
    pil_img_resized.paste(watermark_img_resized,(x,y))
    # Create a Canvas widget and display the watermarked image
    canvas.delete("all")  # Clear existing drawings
    tk_img = ImageTk.PhotoImage(pil_img_resized)
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
    canvas.image = tk_img  # Keep a reference to the image to prevent it from being garbage collected

    pil_img_with_watermark = pil_img_resized
    # Enable the download button to allow downloading
    download_button.config(state=tk.NORMAL)




def input_watermark_image():
    def submit_img_watermark():
        f_types = [('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        watermark_img = Image.open(filename)
        watermark_img_resized = watermark_img.resize((100, 100))
        window.destroy()  # Close the input window
        insert_img_watermark(watermark_img_resized)
        


    window = tk.Tk()
    window.geometry("500x600")  # Adjusted the height for image display
    window.title('Upload image watermark')

    my_font1 = ('times', 18, 'bold')
    l1 = tk.Label(window, text='Image', width=30, font=my_font1)
    l1.grid(row=1, column=1)

    # Create a Canvas widget to display the image
    canvas = tk.Canvas(window, width=400, height=400)
    canvas.grid(row=2, column=1)

    b1 = tk.Button(window, text='Upload image watermark', width=20, command=submit_img_watermark)
    b1.grid(row=3, column=1)





##OPTION TO SELECT TEXT OR IMAGE WATERMARK
def watermark_selection():
    def submit_txt_selection():
        watermark_selection_window.destroy()
        input_watermark_txt()
    
    def submit_img_selection():
        watermark_selection_window.destroy()
        input_watermark_image()


    # Create the watermark selection window
    watermark_selection_window = tk.Tk()
    watermark_selection_window.title("Watermark Input")

    # Create a Label widget for instructions
    instruction_label = tk.Label(watermark_selection_window, text="Select text or image watermark")
    instruction_label.pack(pady=10)

    text_button = tk.Button(watermark_selection_window, text="Text watermark", command=submit_txt_selection)
    text_button.pack(pady=10)

    image_button = tk.Button(watermark_selection_window, text="Image watermark", command=submit_img_selection)
    image_button.pack(pady=10)

    # Start the Tkinter loop for just watermark window
    watermark_selection_window.mainloop()








# MAIN WINDOW FOR DESKTOP APP.
window = tk.Tk()
window.geometry("500x600")  # Adjusted the height for image display
window.title('Image Watermarking Desktop App')

# UI components
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(window, text='Image', width=30, font=my_font1)
l1.grid(row=1, column=1)

# Create a Canvas widget to display the image
canvas = tk.Canvas(window, width=400, height=400)
canvas.grid(row=2, column=1)

b1 = tk.Button(window, text='Upload File', width=20, command=watermark_selection)
b1.grid(row=3, column=1)

# Create a Download button
download_button = tk.Button(window, text='Download Watermarked Image', width=30, command=download_image, state=tk.DISABLED)
download_button.grid(row=4, column=1)

window.mainloop()



