#upload a picture of a clothing

#take a picture with the camera and save it as an image
import cv2
import matplotlib.image as img

from colorthief import ColorThief

from scipy.spatial import KDTree
import colorsclothes

from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb
)
    



cap = cv2.VideoCapture(0)

while True:
    #reads image
    ret, frame = cap.read()

    #shows image
    cv2.imshow("press space when you want to take the picture", frame)

    key = cv2.waitKey(1)
    
    #esc
    if key==27:
        break

    #space
    elif key==ord(' '): 
        #writes image to this file
        cv2.imwrite("/Users/ayushsawnani/Documents/Code/PYTHON/clothestylr/clothing_image.png", frame)
        break 

cap.release()
cv2.destroyAllWindows()


#find the dominant color name
clothing_image = img.imread('clothing_image.png')

color_thief = ColorThief('clothing_image.png')
dominant_color = color_thief.get_color(quality=1)

css3_db = CSS3_HEX_TO_NAMES
names = []
rgb_values = []
for color_hex, color_name in css3_db.items():
    names.append(color_name)
    rgb_values.append(hex_to_rgb(color_hex))

kdt_db = KDTree(rgb_values)
distance, index = kdt_db.query(dominant_color)
print(names[index])

color = names[index]



#find matching colors
for key in colorsclothes.colors.keys():
    if key in color:
        print("Matching colors:")
        for color in colorsclothes.colors[key]:
            print(color)

        break







