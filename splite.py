import os
from PIL import Image


for file in os.listdir('./'):
    if file.endswith(".png"):
        input_1 = file
        print(f"File {input_1} is found")
        im = Image.open(input_1)
        x_width, y_height = im.size
        split = int(y_height/x_width)
        outputFileFormat = "{0}_{1}.png"
        baseName = file.split(".png")[0]
        outputPath = "./"+baseName+"/"
        for i in range(1, split+1):
            x = x_width * (i-1)
            box = (0, x,x_width, x_width*i)
            a = im.crop(box)
            a.load()
            os.makedirs(outputPath, exist_ok = True)
            outputName = os.path.join(outputPath, outputFileFormat.format(baseName, i ))
            a.save(outputName)