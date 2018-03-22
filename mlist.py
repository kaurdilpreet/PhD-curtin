#!/usr/bin/env python

import os
import subprocess


directory = '/home/dilpreet/python/Data'
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        print(os.path.join(directory, filename))
        subprocess.Popen(["unlink", "directory + filename"])




