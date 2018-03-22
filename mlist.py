#!/usr/bin/env python

import os
import subprocess


directory = '/home/dilpreet/python/Data'
for filename in os.listdir(directory):
    if filename.endswith(".py"):
        print(os.path.join(directory, filename))
        test = os.path.join(directory, filename)
        subprocess.call(["unlink", test])




