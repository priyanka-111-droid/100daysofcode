# Image Watermarking Desktop App

## Prerequisites

Tkinter - for GUI of App

Pillow Library - for Image manipulation
```
pip install pillow
```

## Approach

- Create a new directory and create a virtual environment to activate it.
```
mkdir python-desktop-app
cd python-desktop-app
python -m venv venv
source venv/bin/activate  # Linux and macOS
venv\Scripts\activate     # Windows
```
    
- First we assumed only text watermark involved.Also assume that watermark is a fixed value , say "ABCD".
- Make main window using Tkinter with button to upload image, canvas to display watermarked image and button to download watermarked image(initially,download must be disabled)
- When you click upload button, it should go to upload_file function.
- Now use Tkinter filedialog to upload image file from local file directory. Refer https://www.plus2net.com/python/tkinter-filedialog-upload-display.php
- Resize image and go to insert_text_watermark() where you can set font color,font style(download free donts from https://www.fontspace.com/category/ttf),position of watermark and then draw the watermark. Return this watermarked image.
- Display watermarked image in upload_file() and enable the download button so that user can download now.
 
### First enhancement
- Now we are letting user enter any text he wants as watermark text.
- make a function input_watermark_txt()
- create new Tkinter watermark_window,make text field in watermark_window for user input(Entry widget),button to submit.
- In submit_watermark(), ensure you capture the user input,destroy the watermark_window and then pass this user input argument to upload_file(watermark_txt). 


```
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
```



### Second enhancement
- Now we want to give option to upload watermark as text or watermark as image(logo).
- When we click the Upload File option in the main window, it leads to watermark_selection() window.
    - If user selects text watermark,destroy this watermark_selection_window and go to input_watermark_txt().
    - If user selects image watermark,destroy this watermark_selection_window and go to input_watermark_image().
        - Select watermark image(logo) from file system and resize to 100x100 size
        - Select original image from file system on which you want watermark to be placed and resize to 400x400 size. 
        - Refer https://python.plainenglish.io/the-latest-way-for-adding-text-or-image-watermark-using-python-pillow-library-ec7277880080

        