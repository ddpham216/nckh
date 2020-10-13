

from PIL import Image, ImageDraw, ImageFont
import random

number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alphabet_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


#add margin to image
def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result
# Random generate Captcha
def create_random_captcha_text(captcha_string_size=1):
    captcha_string_list = []
    base_char = alphabet_lowercase + alphabet_uppercase + number_list

    for i in range(captcha_string_size):
        # Select one character randomly.
        char = random.choice(base_char)

        # Append the character to the list.
        captcha_string_list.append(char)

    captcha_string = ''

    # Change the character list to string.
    for item in captcha_string_list:
        captcha_string += str(item)

    return captcha_string

# Create an image captcha with special text.
def create_image_captcha(text,font_ttf,font_size,IMG_WIDTH,IMG_HEIGHT):
    image = Image.new("RGB", (64, 64),  color=(0, 0, 0))
    font = ImageFont.truetype(font_ttf, font_size)
    draw = ImageDraw.Draw(image)
    w, h = draw.textsize(text, font=font)
    #middle-align character
    X=(IMG_WIDTH - w) / 2
    Y=(IMG_HEIGHT - h) / 2
    draw.text((X, Y), captcha_text, font=font, fill=(255, 255, 255))
    # draw.text((20, 20), text, font=font, fill=(255, 255, 255))
    image_file = text + ".png"
    image.save(image_file)
    print(image_file + " has been created.")
# #generate captcha with check code
#     image = add_margin(img,0, 0, 20, 0, (255, 255, 255))
#     draw = ImageDraw.Draw(image)
#     draw.text((65, 65),captcha_text,(0,0,0))
#     # Save the image to a png file.

if __name__ == '__main__':
    #gen 10 captcha
    for i in range (1):
    # Create random text.
        captcha_text = create_random_captcha_text()
    # Create image captcha.
        create_image_captcha(captcha_text,"FreeMono.ttf",font_size= 64, IMG_WIDTH=64,IMG_HEIGHT=64)
