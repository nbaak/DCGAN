#!/usr/bin/env python3 

import os
import gdown
from zipfile import ZipFile

os.makedirs("celeba_gan",  exist_ok=True)
os.makedirs("gen_images" , exist_ok=True)

url = "https://drive.google.com/uc?id=1O7m1010EJjLE5QxLZiM9Fpjs7Oj6e684"
output = "celeba_gan/data.zip"
gdown.download(url, output, quiet=True)

with ZipFile("celeba_gan/data.zip", "r") as zipobj:
    zipobj.extractall("celeba_gan")
