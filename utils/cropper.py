#!/usr/bin/env python

import os
import sys
from PIL import Image, ImageChops, ImageOps
from time import time

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

RAW_CHORDS = os.path.join(THIS_DIR, 'chords-raw')
CROPPED_CHORDS = os.path.join(THIS_DIR, 'chords-cropped')


def trim(img):
    bg = Image.new(img.mode, img.size, img.getpixel((0,0)))
    diff = ImageChops.difference(img, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return img.crop(bbox)


def resize(im, color=None):
    color = color or (255, 255, 255)
    width, height = im.size
    new_width = width - 10
    im.thumbnail((new_width, height), Image.ANTIALIAS)
    new_width, new_height = im.size

    center = (
        int(round(width - ((width + new_width) / 2))),
        int(round(height - ((height + new_height) / 2))),
        )

    bg = Image.new(im.mode, (width, height), color)
    bg.paste(im, center)
    return bg


def pad(im, border=20):
    im = ImageOps.expand(im, border, (255, 255, 255))
    return im


def main():
    start_time = time()
    num_images = 0

    images = filter(lambda f: f.endswith('.png'), os.listdir(RAW_CHORDS))
    for filename in sorted(images):
        print(filename)
        raw_path = os.path.join(RAW_CHORDS, filename)
        cropped_path = os.path.join(CROPPED_CHORDS, filename)

        img = Image.open(raw_path)
        img = trim(img)
        img = trim(img)
        # img = resize(img)
        img = pad(img, (40, 30))
        img.save(cropped_path)

    end_time = time()
    print('{0} images cropped in {1} seconds'.format(num_images, end_time - start_time))

if __name__ == '__main__':
    main()
