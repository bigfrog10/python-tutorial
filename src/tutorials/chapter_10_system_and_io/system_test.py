import sys
import os
import webbrowser

# os level
print(os.name)  # nt
print(sys.platform)  # win32
print(sys.byteorder)  # little or big indian
# print(os.environ['name'])
print(os.environ)  # key-value depends on os
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')

import getpass
print(getpass.getuser())

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

import platform
print(platform.system())  # Windows
print(platform.release())  # 10

print(sys.getrecursionlimit())  # 1000

from subprocess import call
call(["ls", "-l"])

import multiprocessing
print(multiprocessing.cpu_count())

import time
print("Last modified: %s" % time.ctime(os.path.getmtime("notes.txt")))
print("Created: %s" % time.ctime(os.path.getctime("notes.txt")))
print(os.path.getsize("notes.txt"))

str1 = "one"
str2 = "four"
str3 = "three"
print()
print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")

if __name__ == '__main__':
    args = sys.argv
    print(args)

    # open the default browser
    # The wield thing: run this here will open firefox; run this in cmd, it opens ie8.
    # my default is firefox
    res = webbrowser.open('http://www.youtube.com')  # open default browser
    print(res)  # True


