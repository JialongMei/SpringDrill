from PIL import Image

def recolor(url):
    image = Image.open(url).convert("RGBA")
    new_image = Image.new("RGBA", image.size, "BLACK")
    new_image.paste(image, mask=image)

    return new_image.convert("RGB")
