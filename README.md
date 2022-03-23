# CarbonPy

Use Carbon from terminal to generate images of your source code

![GitHub](https://img.shields.io/github/license/leugimkm/carbonpy)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](./code_of_conduct.md)
![GitHub languages](https://img.shields.io/github/languages/top/leugimkm/carbonpy)
![GitHub repo size](https://img.shields.io/github/repo-size/leugimkm/carbonpy)
![Github last-commit](https://img.shields.io/github/last-commit/leugimkm/carbonpy)
![maintenance](https://img.shields.io/maintenance/yes/2022)

       __|            |                 _ \      
      (      _` |   _| _ \   _ \    \   __/ |  | 
     \___| \__,_| _| _.__/ \___/ _| _| _|  \_, | 
                                           ___/  

`carbonpy` is a simple tool to generate an image from a local file or
from a GitHub repository. It can also be used to send the source code
to carbon.now.sh and generate the image there.

# Installation

`carbonpy` is available on [PyPi](https://pypi.org/project/carbonpy/) (MIT license)
and installation can be performed by running [pip](https://docs.python.org/es/3/installing/index.html)

```
python -m pip install carbonpy
```
To upgrade the package:
```
python -m pip install carbonpy --upgrade
```
To delete the package:
```
python -m pip uninstall carbonpy
```

# Example

To generate an image from a local file:

    > python -m carbonpy main.py -s
    Done!
    Image created in current directory: main.png

To generate an image from a GitHub repository:

    > python -m carbonpy soluciones/fibonacci.py -g
    Done!
    Image created in current directory: fibonacci.png

You can also send the content of the source code to carbon.now.sh:

    > python -m carbonpy main.py -c
    Sent to Carbon.now.sh

    > python -m carbonpy soluciones/fibonacci.py -gc
    Sent to Carbon.now.sh

Help command:

    > carbonpy -h

or:

    > carbonpy --help


# Contribution

If you'd like to contribute, fork the repository, commit your changes to main branch 
and send a pull request.
Make sure you add yourself to authors.