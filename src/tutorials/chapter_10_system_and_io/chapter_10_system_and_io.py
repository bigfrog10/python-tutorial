
# with context
from PIL import Image

# https://pymotw.com/3/contextlib/

with open("notes.txt") as f:
    data = f.read()
    print(data)

try:
    f = open("notes.txt")
    data = f.read()
    print(data)
finally:
    f.close()

with open('output.txt', 'w') as f:
    f.write('hello world')

with open('panda.jpg', 'rb') as f:
    s = f.read()

with Image.open('panda.jpg') as image:
    print(image.size)
    image.show()

# file
import glob
import os
import pprint

# https://www.makeuseof.com/tag/mac-terminal-commands-cheat-sheet/
print(glob.glob("/Users/yupingcui/IdeaProjects/ashleytutorial1/*"))
print(glob.glob("/Users/yupingcui/*.m4r"))
# print(os.environ['HOME'])  # mac
# print(os.environ['USER'])
pprint.pprint(dict(os.environ), width=1)

import sys
# python level - here sys = python
print(sys.version)  # python version
print(sys.executable)  # python executable path. Use PYTHONHOME to modify this

pprint.pprint(sys.path)  # python lib search paths. Use PYTHONPATH to modify this
print(sys.modules)
print(sys.builtin_module_names)
print(os.environ['PYTHONPATH'])

# sys.stdout, sys.err, sys stdin redirect
# serialization/pickle

# argparse

# gc

# concurrency, GIL

# https://preshing.com/20110920/the-python-with-statement-by-example/
