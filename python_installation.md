## python installation
official download  
https://www.python.org/downloads/  
Python installation is a little bit tricky comparing to Java, because of the 
C/C++ dependent libraries. Python itself installation is good to go, but some
of the 3rd party libraries require OS dependent compilation. This compilation
causes trouble and difficulty for developers. Anaconda pre-compiles these 
libraries for certain OS platforms and bundle them for installation. 

Secondly, since 3rd party libs are installed to the Python home directory, 
it’s very likely we run into all kind of conflicts from different packages as
we install more and more packages. To avoid this problem, we create isolated
Python environments for different purposes. Pip and Anaconda both can create
virtual environments.

## miniconda installation
The official Miniconda site is: https://docs.conda.io/en/latest/miniconda.html. 
It contains only conda, Python, and small number of essential packages.

Download the 64 bit latest version and Python 3 for your target OS. Before 
installation, unset PYTHONHOME and PYTHONPATH first.

We refer the installation directory as %CONDA_INSTALL% throughout this 
document.

If needed, set HTTP proxy as well(set for windows, export for linux/mac):
```
set HTTP_PROXY=<proxy server>:<port>
set HTTPS_PROXY=<proxy server>:<port>
```

Here are some useful commands, also check out the cheat sheet: 
https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html  
for example:
```
(clown) WonderfuliMac-3627:~ ***$ conda info
 
     active environment : clown
    active env location : /Users/***/.conda/envs/clown
            shell level : 2
       user config file : /Users/***/.condarc
 populated config files : 
          conda version : 4.8.2
    conda-build version : 3.18.11
         python version : 3.7.6.final.0
       virtual packages : __osx=10.15.6
       base environment : /opt/anaconda3  (writable)
           channel URLs : https://repo.anaconda.com/pkgs/main/osx-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/osx-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /opt/anaconda3/pkgs
                          /Users/***/.conda/pkgs
       envs directories : /opt/anaconda3/envs
                          /Users/***/.conda/envs
               platform : osx-64
             user-agent : conda/4.8.2 requests/2.22.0 CPython/3.7.6 Darwin/19.6.0 OSX/10.15.6
                UID:GID : 501:20
             netrc file : None
           offline mode : False
```
To make sure conda has latest version  
```conda update conda```

To make sure pip is update to date (pip is the Python installer and used internally by conda)  
```python –m pip install --upgrade pip```

## python virtual environments  
Miniconda is shared across environments. A good reference is: 
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

To list current environments:  
```
conda env list
conda info --env
```

To create a new environment with name py366_clown and python environment 3.6.6:  
```conda create --name py366_clown python=3.6.6```

To create a new environment with all Anaconda default packages:  
```conda create --name py366_clown anaconda python=3.6.6```

To activate the new environment:
```
C:\>activate py366_clown
(py366_clown)C:\>
```

To deactivate the environment:
```
(py366_clown)C:\>deactivate
C:\>
```

But as mentioned below, we should use conda version of these:
```
conda activate my_env
conda deactivate
```

There is a convenient UNIX command package, install it if you choose so:  
```conda install -c anaconda unxutils```  
This will be installed into the $PYTHONHOME\Scripts folder.

This is to install from known channel anaconda. If your setting is routed to an
internal repo, we need to give the full URL. Otherwise, use the suffix:  
```conda install unxutils –c https://conda.anaconda.org/anaconda```

Since Anaconda does not have all Python packages, sometimes we still need to 
use pip to install.  
```pip install <package> -i https://pypi.org/simple```

To install a particular version(use double = sign):  
```pip install tensorflow==1.15.2 -i https://pypi.org/simple```

To install from a local folder using pip:  
```pip install <local folder with setup.py>```

To install from a local folder using conda  
```conda install c:\download\unxutils-14.04.03-0.tar.bz2```  
This file is downloaded from http://anaconda.org/anaconda/unxutils/files

The local package cache is $CONDA_INSTALL\pkgs to avoid repetitive downloads.

To generate requirements.txt using pip:  
```pip freeze > requirements.txt```

To install from the requirements.txt using pip  
```pip install –r requirements.txt```

To export a conda environment file:
```conda env export > my_conda.yaml```

This file separates the pip packages and conda packages, so we don’t have the 
issue above. This file can be used to create other environments with the same
name embedded in the YAML file  
```conda env create –-file my_conda.yaml```

This is used to copy someone else environment to local machine.
To update existing env with this file:  
```conda env update –n my_new_env –f my_conda.yaml```  

If needed, add -i https://pypi.org/simple to the first line in pip section. 
Or more complicated, we can add more pip switches in the YAML file:
```
dependencies:
    - pip:
        - --index-url https://pypi.org/simple
        - --extra-index-url https://pypi.myorg/simple 
```

We can also add channel to the YAML file:
```
channels:
    - defaults
    - conda-forge::beautifulsoup4
    - https://conda.anaconda.org/anaconda
```

To clone an environment:  
```conda create --name my_env_clone --clone my_env ```

To remove an environment:  
```conda env remove –n my_env```

To print the dependency tree of any library, check out this tool:  
https://github.com/wimglenn/johnnydep

##Suggested Practices
Among several ways, we suggest the following installation path:
1. Install Miniconda package (containing conda, Python, pip and other tools)
2. Use conda to create new virtual environment
3. Use conda to install libraries, check anaconda, forge-conda channels, or 
others.
4. If anaconda does not have the package, use pip.
5. In a project, we need to manually maintain requirements.txt for all 
dependent libs. Keep it minimal, not include all dependencies of these 
libraries. IntelliJ helps the label since it tracks the content of this file. 
In a new environment, use pip to install this file.
6. If any dependent library requires anaconda package, use conda.yaml generated
from conda env export. But IntelliJ does not know this format.
7. In other cases, create either pip package or conda package.  

When install a package with soft link, use pip install –e.  
This is for the case where you develop an internal package and you want to link
your Python source code to the virtual environment. Once you modify your code, 
the calling code can see the change right away (so you don’t need to install
the package with the change again).