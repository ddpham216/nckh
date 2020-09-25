import string
import os
import cv2 as cv
import numpy as np

IMG_HEIGHT = 28
IMG_WIDTH = 28
FONT = [
    cv.FONT_HERSHEY_SIMPLEX,
    cv.FONT_HERSHEY_DUPLEX,
    cv.FONT_HERSHEY_COMPLEX,
    cv.FONT_HERSHEY_TRIPLEX,
    cv.FONT_HERSHEY_SCRIPT_SIMPLEX,
    cv.FONT_HERSHEY_SCRIPT_COMPLEX,
    cv.FONT_ITALIC
]
FONT_SCALE = [0.6, 0.7, 0.8, 0.9]
FONT_COLOR = 255
THICKNESS = [1]
LINE_TYPE = [0, 1, 2, 3]


def generate_char(list_character):
    count = 0
    for c in list_character:
        for f in FONT:
            for fs in FONT_SCALE:
                for t in THICKNESS:
                    for lt in LINE_TYPE:
                        img = np.zeros((28, 28, 1), np.uint8)
                        text_size = cv.getTextSize(c, f, fs, t)[0]
                        text_y = int((img.shape[1] - text_size[0]) / 2)
                        text_x = int((img.shape[0] + text_size[1]) / 2)
                        img = cv.putText(img, c, (5, 20), f, fs, FONT_COLOR, t, lt)
                        path = os.path.join(os.getcwd(), 'img', str(list_character.index(c)))
                        if os.path.exists(path):
                            pass
                        else:
                            os.mkdir(path)
                        cv.imwrite(path + '\\{0}.jpg'.format(count), img)
                        count += 1


if __name__ == '__main__':
    list_character = string.ascii_letters + string.digits
    generate_char(list_character)
    print(list_character)
