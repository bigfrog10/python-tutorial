## Package Builds
A setup.py is needed in the source folder, with packages and install_requires
specified. (Need to specify packages and all submodules to be included). Then
we can build the packages in several ways:
1. Update needed tools: pip install --upgrade setuptools wheel
2. To build package with source code: python setup.py sdist
3. To build package with wheel binaries: python setup.py bdist_wheel
4. To build package with egg binaries: python setup.py bdist_egg
5. To build package without source code: python setup.py bdist_egg 
--exclude-source-files  

There are four tools that need dependency.  
1. Conda
2. Pip
3. setup.py
4. IDE

The package is in the dist folder.

PyInstaller is a good tool to convert Python code to binary executables, for
performance and obfuscation. Cython is another tool to compile Python code to
shared libraries.