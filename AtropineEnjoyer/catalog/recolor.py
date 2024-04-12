from PIL import Image

def recolor(url):
    image = Image.open(url)
    width, height = image.size
    new_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    new_image.paste(image, (0, 0), image)
    new_image.save("output_image.png")
