#!/usr/local/bin/python
# coding=utf-8

import PIL
from PIL import ImageFont, Image, ImageDraw
import sys
import os

front_file = os.path.expanduser('~/projects/idlimit/yyzz_front.jpg')

font = ImageFont.truetype('/Library/Fonts/Songti.ttc', 90)

im = Image.open(front_file)
# im = im.rotate(270)
draw = ImageDraw.Draw(im)
draw.text((1100,715), u"仅供"+sys.argv[1].decode('utf-8')+u"使用——", (255, 255, 255), font=font)

im.save(os.path.expanduser('~/Documents/upload_yyzz_front.jpg'))

