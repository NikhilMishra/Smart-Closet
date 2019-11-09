import json
import webcolors
import text2speech
from playsound import playsound
import math
# createDict method

# empty dictionary of closet items
closetItems = {
    "ffffff, pant": ["000000, shirt"],
    "000000, pant": ["ffffff, shirt"],
    "663300, pant": ["191970, shirt"],
    "006400, pant": ["a9a9a9, shirt"],
    "ff0000, pant": ["ffff00, shirt"],
    "006600, pant": ["000000, shirt"],
    "ff69b4, pant": ["708090, shirt"],
    "ffffff, shirt": ["000000, pant"],
    "000000, shirt": ["ffffff, pant"],
    "663300, shirt": ["191970, pant"],
    "006400, shirt": ["a9a9a9, pant"],
    "ff0000, shirt": ["ffff00, pant"],
    "006600, shirt": ["000000, pant"],
    "ff69b4, shirt": ["708090, pant"]
}

# dictionary for colors
color = {
    # white to blue, red, black
    "FFFFFF": ["0000FF", "FF0000", "000000"],
    # red to yellow, white,
    "FF0000": ["FFFF00", "FFFFFF"],
    # brown to cream, green
    "663300": ["FFFFCC", "006600"],
    # orange to blue, white, black
    "FFA500": ["0000FF", "FFFFFF", "000000"],
    # green to black, brown
    "006600": ["000000", "663300"]
}

# dictionary for items
items = {
    "pant": "shirt",
    "shirt": "pant"
}

"""adds to dictionary as items are added.
    key = color + value"""

def getClosestColor(input):
    value = input.split(', ')
    color = tuple(int(value[0][i:i+2], 16) for i in (0, 2, 4))
    # color = webcolors.hex_to_rgb(value[0])
    item = value[1]
    print("input" + item)
    (r1,g1,b1) = color
    min = 9999999999
    returnVal = input
    keys = closetItems.keys()
    for i in range(len(closetItems)):
        value1 = list(keys)
        value2 = value1[i].split(', ')
        color1 = value2[0]
        item1 = value2[1]
        (r2,g2,b2) = tuple(int(color1[i:i+2], 16) for i in (0, 2, 4))
        if (math.sqrt((r1 - r2)**2 + (g1 - g2) ** 2 + (b1 - b2) **2)) < min and item1 == item:
            print("in if")
            print(item1 + ' ' + item)
            min = math.sqrt((r1 - r2)**2 + (g1 - g2) ** 2 + (b1 - b2) **2)
            returnVal = closetItems[value1[i]]

    return returnVal

def addDict(closetItems, key):
    closetItems[key] = createsValue(key)


def createsValue(key):
    value = key.split(', ')
    newColor = color.get(value[0])
    newItem = items.get(value[1])
    newValue = newColor[0] + ', ' + str(newItem)
    return newValue

#INPUT COLOR find closest value in closetItems dictionary

def addArray(array, article):
    #rgb = (int(float(array[0])), int(float(array[1])), int(float(array[2])))
    rgb = tuple(array)
    hex_result = '%02x%02x%02x' % rgb
    print(hex_result)
    input = hex_result + ', ' + article
    item = getClosestColor(input)
    recommendation = item
    print(recommendation)
    value = recommendation[0].split(', ')
    color = value[0]
    item = value[1]
    print("Wear a " + webcolors.hex_to_name('#' + color) + " " + item)
    subscription_key = "3dcb81c95f9d46248813f574677f3272"
    app = text2speech.TextToSpeech(subscription_key, webcolors.hex_to_name('#' + color), article)
    app.get_token()
    app.save_audio("suggestion.wav")
    playsound('suggestion.wav')



def main():
    print("Hello!")

# userInputColor = input("What color (hex) is your item?")
# # userInputColorHex = str('#{:02x}{:02x}{:02x}'.format(userInputColor))
# rgb = (255, 255, 255)
# hex_result = "".join([format(val, '02X') for val in rgb])
# userInputItem = str(input("What item is it?"))
# input = hex_result + ', ' + str(userInputItem)
# addDict(closetItems, input)
# print(closetItems)
# recommendation = closetItems.get(input)
# value = recommendation.split(', ')
# color = value[0]
# item = value[1]
#
# print("Wear a " + webcolors.hex_to_name('#' + color) + " " + item)
