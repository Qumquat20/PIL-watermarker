import os, os.path
import sys
import random
from PIL import Image, ImageEnhance

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

def delete_line():
	sys.stdout.write(CURSOR_UP_ONE)
	sys.stdout.write(ERASE_LINE)

def get_total(filesDir):
    total = 0

    with os.scandir(filesDir) as files:
        for filename in files:
            if filename.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                total += 1
    
    return total

def main():
    c = 0

    markPath = "./bruh.png"
    filesDir = sys.argv[1]

    if os.path.exists(filesDir+"/Marked"):
        pass
    else:
        os.mkdir(filesDir+"/Marked")

    #heights = [0.50,0.51,0.52,0.53,0.54,0.55]
    #widths = [0.25,0.26,0.27,0.28,0.29,0.30]

    randY = [1.85,1.9,2.0]       
    
    with os.scandir(filesDir) as images:
        for image in images:
            if image.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                c += 1
                print("Marked ",c,"/",get_total(filesDir))
                delete_line()

                #markHeight = random.choice(heights)
                #markWidth = random.choice(widths)

                markHeight = 1
                markWidth = 0.64

                pasteHeight = random.choice(randY)
                #pasteHeight = 2.05

                img = Image.open(image.name)
                img2 = ImageEnhance.Brightness(img)
                img = img2.enhance(1.2)
                img = img.transpose(Image.ROTATE_90)
                
                # This math is to keep the watermark proportional
                markNewSize = int(img.width * markHeight),int(img.height * markWidth)
                mark = Image.open(markPath)
                mark = mark.resize(markNewSize)

                # The math here is to center the the watermark
                img.paste(mark,((img.width - mark.width) // 2, int((img.height - mark.height) // pasteHeight)), mask=mark)
                img.save((filesDir+"/Marked/"+image.name))
            else:
                pass

if __name__ == "__main__":
    main()
