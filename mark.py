import os, os.path
import sys
import random
from PIL import Image, ImageEnhance

def main():
    markPath = "C:/Users/jenni/OneDrive/Desktop/MARK/bruh.png"
    filesDir = sys.argv[1]

    if os.path.exists(filesDir+"/Marked"):
        pass
    else:
        os.mkdir(filesDir+"/Marked")

    heights = [0.50,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.60]
    widths = [0.25,0.26,0.27,0.28,0.29,0.30,0.31,0.32,0.33,0.34,0.35]

    for root, dirs, files in os.walk(filesDir):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                markHeight = random.choice(heights)
                markWidth = random.choice(widths)

                img = Image.open(filename)
                img2 = ImageEnhance.Brightness(img)
                img = img2.enhance(1.25)
                img = img.transpose(Image.ROTATE_90)
                
                markNewSize = int(img.width * markHeight),int(img.height * markWidth)
                mark = Image.open(markPath)
                mark = mark.resize(markNewSize)

                img.paste(mark,((img.width - mark.width) // 2, int((img.height - mark.height) // 2)), mask=mark)
                img.save((filesDir+"/Marked/"+filename), format="png")
            else:
                pass

if __name__ == "__main__":
    main()