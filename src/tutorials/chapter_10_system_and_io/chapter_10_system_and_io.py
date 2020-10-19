
# with context
from PIL import Image

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


# sys.stdout, sys.err, sys stdin redirect
# serialization/pickle

# argparse

# gc

# concurrency, GIL
