import sys
import os
import webbrowser

if __name__ == '__main__':
    args = sys.argv
    print(args)
    print(os.environ['name'])
    print(os.environ)

    webbrowser.open('http://www.youtube.com')