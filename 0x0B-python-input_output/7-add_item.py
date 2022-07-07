#!/usr/bin/python3
"""Module that adds all arguments to a python list,
and then saves them to a file

Use your function ``save_to_json_file`` from ``5-save_to_json_file.py``
Use your function ``load_from_json_file`` from ``6-load_from_json_file.p``y
"""

import sys
import os.path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
my_list = []

if os.path.exists(filename) and os.path.getsize(my_file) > 0:
    my_list = load_from_json_file(filename)

    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            my_list.append(arg)

save_to_json_file(my_list, filename)
