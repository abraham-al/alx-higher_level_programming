#!/usr/bin/python3
"""
adds all arguments to a Python list
"""
import sys


save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", "a")
try:
    i = load("add_item.json")
except ValueError:
    i = []
save(i + sys.argv[1:], "add_item.json")
