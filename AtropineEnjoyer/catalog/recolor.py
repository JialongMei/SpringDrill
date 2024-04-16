from PIL import Image
import os


#black the background for entire folder of images
def recolor(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        image = Image.open(file_path).convert("RGBA")
        new_image = Image.new("RGBA", image.size, "BLACK")
        new_image.paste(image, mask=image)
        recolored_image = new_image.convert("RGB")
        recolored_image.save(file_path)

    return 0

recolor("C:\\Users\\Narea\\Downloads\\icons")
