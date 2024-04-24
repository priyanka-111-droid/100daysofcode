import os
import numpy as np
from PIL import Image
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = "C:\\"
app.config['MAX_CONTENT_PATH'] = 1000000

@app.route('/')
def home():
 return render_template("index.html")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        f = request.files['file']
        filename = secure_filename(f.filename)

    if len(filename) > 1:
        fullpath = os.path.join(filename)
        f.save(fullpath)
        palette_hex, palette_rgb = get_colors_in_image(fullpath)
        return render_template("index.html", hex_success=True, palette_hex=palette_hex, palette_rgb=palette_rgb)

    return render_template("index.html")


def get_colors_in_image(filepath):
    def rgb_to_hex(r, g, b):
        ans = ('{:X}{:X}{:X}').format(r, g, b)

        while len(ans) < 6:
            ans = "0" + ans

        return "#" + ans

    def hex_to_rgb(h):
        rgb = []
        for i in (0, 2, 4):
            decimal = int(h[i:i + 2], 16)
            rgb.append(decimal)

        return tuple(rgb)

    def get_top_10(hex_list):
        hex_frequency = {}

        for item in hex_list:
            if item in hex_frequency:
                hex_frequency[item] += 1
            else:
                hex_frequency[item] = 1

        sorted_hex = dict(sorted(hex_frequency.items(), key=lambda item: item[1]))

        return list(sorted_hex.keys())[-10:][::-1]

    image_file = Image.open(filepath)
    image_array = np.array(image_file)

    shape = image_array.shape

    x = shape[0]
    y = shape[1]

    hex_list = []
    for x in range(x):
        for y in range(y):
            rgb = image_array[x, y, :]

            r = rgb[0]
            g = rgb[1]
            b = rgb[2]

            hex_list.append(rgb_to_hex(r, g, b))

    top_10_hex = get_top_10(hex_list)
    top_10_rgb = [hex_to_rgb(i[-6:]) for i in top_10_hex]

    return top_10_hex, top_10_rgb


if __name__ == "__main__":
    app.run(debug=True)