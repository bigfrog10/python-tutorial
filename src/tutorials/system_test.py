import sys
import os
import webbrowser

if __name__ == '__main__':
    args = sys.argv
    print(args)

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
    webbrowser.open('http://www.youtube.com')

    import keyword
    print(keyword.kwlist)
