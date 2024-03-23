#it imports colors from the image
import colorgram

rgb_colors = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
