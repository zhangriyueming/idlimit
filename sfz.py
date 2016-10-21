#!/usr/local/bin/python
# coding=utf-8

import PIL
from PIL import ImageFont, Image, ImageDraw
import sys
import os

front_file = os.path.expanduser('~')+"/projects/idlimit/sfz_front.jpg"
back_file = os.path.expanduser('~')+"/projects/idlimit/sfz_back.jpg"

font = ImageFont.truetype('/Library/Fonts/Songti.ttc', 40)

im = Image.open(front_file)
draw = ImageDraw.Draw(im)
draw.text((100,715), u"仅供"+sys.argv[1].decode('utf-8')+u"使用——", (255, 255, 255), font=font)

im.save(os.path.expanduser('~')+'/upload_front.jpg')

im = Image.open(back_file)
draw = ImageDraw.Draw(im)
draw.text((130,715), u"仅供"+sys.argv[1].decode('utf-8')+u"使用——", (255, 255, 255), font=font)

im.save(os.path.expanduser('~')+'/upload_back.jpg')

