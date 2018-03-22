#!/usr/bin/env python

import os
import subprocess


directory = '/Users/dilpreetkaur/Documents/python/Data'
for filename in os.listdir(directory):
    if filename.endswith(".py"):
        test= os.path.join(directory, filename)       
	subprocess.Popen(["unlink", test])




