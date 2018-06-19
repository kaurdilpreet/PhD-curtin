#!/usr/bin/env python

"""Script for cleaning space in group/astro/scratch

"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-O', action='store_const', dest='constant_value', const='value-to-store', help='Give obs ID')
parser.add_argument('-o', action='store_const', dest='constant_value', const='value-to-store', help='Give cal obs ID')
parser.add_argument('-t', action='store_const', dest='constant_value', const='value-to-store', help='Give file type')
parser.print_help()


