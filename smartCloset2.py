import os
import webcolors
import text2speech
import closetDict
import camTest
import speech2text
import re
from playsound import playsound
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd  + bd)] = name
    return min_colours[min(min_colours.keys())]
os.environ["Path to JSON"]
print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
from google.cloud import vision
client = vision.ImageAnnotatorClient()
import io
from PIL import Image
camTest.capture()
# Opens a image in RGB mode
im = Image.open('opencv.png')
path = 'opencv.png'
#suggest = input("what article of clothing do you want a suggestion for? ")
subscription_key = "subscription key here"
app = text2speech.TextToSpeech(subscription_key, "none", "none")
app.get_token()
app.save_audio("suggest.wav")
playsound('suggest.wav')
suggest = str(speech2text.userInput())
suggest = re.findall(r'"([^"]*)"', suggest)[0].rstrip('.')
print(suggest)
with io.open(path, 'rb') as image_file:
        content = image_file.read()
image = vision.types.Image(content=content)
objects = client.object_localization(
        image=image).localized_object_annotations
for object_ in objects:
    coord = [];
    i = 0;
    for vertex in object_.bounding_poly.normalized_vertices:
        if i == 0:
            coord.append(vertex.x)
            coord.append(vertex.y)
        if i == 1:
            coord.append(vertex.x)
        if i == 2:
            coord.append(vertex.y)
        i+=1
    if (object_.name == "Top" or object_.name == "Shirt" or object_.name == "Outerwear"):
        width, height = im.size
        # Cropped image of above dimension
        # (It will not change orginal image)
        im1 = im.crop((coord[0]*width, coord[1]*height, coord[2]*width, coord[3]*height))
        im1.save("top.png")
        path = "top.png"
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.image_properties(image=image)
        props = response.image_properties_annotation
        topColor = []
        for color in props.dominant_colors.colors:
            topColor.append(int(float(format(color.color.red))))
            topColor.append(int(float(format(color.color.green))))
            topColor.append(int(float(format(color.color.blue))))
            break

    if (object_.name == "Pants"):
        width, height = im.size
        # Cropped image of above dimension
        # (It will not change orginal image)
        im2 = im.crop((coord[0]*width, coord[1]*height, coord[2]*width, coord[3]*height))
        im2.save("pant.png")

        path = "pant.png"
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.image_properties(image=image)
        props = response.image_properties_annotation
        pantColor = []
        for color in props.dominant_colors.colors:
            pantColor.append(int(float(format(color.color.red))))
            pantColor.append(int(float(format(color.color.green))))
            pantColor.append(int(float(format(color.color.blue))))
            break
if suggest == "Pant" or suggest == "Pants" or suggest == "Paint" or suggest == "Paints":
    for color in topColor:
        print(int(float(color)))
    closetDict.addArray(topColor, "shirt")
else:
    for color in pantColor:
        print(int(float(color)))
    closetDict.addArray(pantColor, "pant")
