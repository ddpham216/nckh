from PIL import Image, ImageDraw, ImageFont
import random
import os


# Create an image captcha with special text.
def create_image_captcha(text, font_ttf, font_size, IMG_WIDTH, IMG_HEIGHT):
    image = Image.new("RGB", (64, 64), color=(0, 0, 0))
    font = ImageFont.load(font_ttf)
    # font = ImageFont.truetype(font_ttf, font_size)
    draw = ImageDraw.Draw(image)
    w, h = draw.textsize(text, font=font)
    # middle-align character
    X = (IMG_WIDTH - w) / 2
    Y = (IMG_HEIGHT - h) / 2
    draw.text((X, Y), text, font=font, fill=(255, 255, 255))
    # draw.text((20, 20), text, font=font, fill=(255, 255, 255))
    image_file = text + ".png"
    image.save(image_file)
    print(image_file + " has been created.")


if __name__ == '__main__':
    f = open("fonts/fonts.list")
    for x in f:
        font = x
        print(font)
        create_image_captcha(text="s", font_ttf=font, font_size=64, IMG_WIDTH=64, IMG_HEIGHT=64)
