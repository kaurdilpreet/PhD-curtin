#!/usr/bin/env python

import os

directory = '/home/dilpreet/python/Data'
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        print(os.path.join(directory, filename))
        os.unlink(os.path.join(directory, filename))



