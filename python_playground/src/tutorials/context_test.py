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

with open('ashley1.txt', 'w') as f:
    f.write('hello world')

with open('panda.jpg', 'rb') as f:
    s = f.read()

with Image.open('panda.jpg') as image:
    print(image.size)
    image.show()
