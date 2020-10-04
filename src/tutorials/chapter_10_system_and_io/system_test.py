import sys
import os
import webbrowser

# os level
print(os.name)  # nt
print(sys.platform)  # win32
print(sys.byteorder)  # little or big indian
# print(os.environ['name'])
print(os.environ)  # key-value depends on os

# python level - here sys = python
print(sys.version)  # python version
print(sys.executable)  # python executable path. Use PYTHONHOME to modify this
print(sys.path)  # python lib search paths. Use PYTHONPATH to modify this
print(sys.modules)
print(sys.builtin_module_names)
print(os.environ['PYTHONPATH'])

import keyword
print(keyword.kwlist)

print(os.getenv('HOMEPATH'))  # depend on OS
print(os.getenv('USERPROFILE'))
print(os.path.expanduser('~'))


if __name__ == '__main__':
    args = sys.argv
    print(args)

    # open the default browser
    # The wield thing: run this here will open firefox; run this in cmd, it opens ie8.
    # my default is firefox
    res = webbrowser.open('http://www.youtube.com')  # open default browser
    print(res)  # True


