# Code2img

Use code2img from terminal to generate images of your source code

![GitHub](https://img.shields.io/github/license/leugimkm/code2img)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](./code_of_conduct.md)
![GitHub languages](https://img.shields.io/github/languages/top/leugimkm/code2img)
![GitHub repo size](https://img.shields.io/github/repo-size/leugimkm/code2img)
![Github last-commit](https://img.shields.io/github/last-commit/leugimkm/code2img)
![maintenance](https://img.shields.io/maintenance/yes/2022)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/leugimkm/code2img)
![PyPI - Format](https://img.shields.io/pypi/format/code2img)
[![Downloads](https://pepy.tech/badge/code2img)](https://pepy.tech/project/code2img)

                                 
               _     ___ _           
     ___ ___ _| |___|_  |_|_____ ___ 
    |  _| . | . | -_|  _| |     | . |
    |___|___|___|___|___|_|_|_|_|_  |
                                |___|


`code2img` is a simple tool to generate an image from a local file or
from a GitHub repository. It can also be used to send the source code
to carbon.now.sh and generate the image there.

# Installation

`code2img` is available on [PyPi](https://pypi.org/project/code2img/) (MIT license)
and installation can be performed by running [pip](https://docs.python.org/es/3/installing/index.html)

```
python -m pip install code2img
```
To upgrade the package:
```
python -m pip install code2img --upgrade
```
To delete the package:
```
python -m pip uninstall code2img
```

# Example

To generate an image from a local file:

    > python -m code2img main.py -s
    Done!
    Image created in current directory: main.png

To generate an image from a GitHub repository:

    > python -m code2img soluciones/fibonacci.py -g
    Done!
    Image created in current directory: fibonacci.png

You can also send the content of the source code to carbon.now.sh:

    > python -m code2img main.py -c
    Sent to Carbon.now.sh

    > python -m code2img soluciones/fibonacci.py -gc
    Sent to Carbon.now.sh

Help command:

    > code2img -h

or:

    > code2img --help


# Contribution

If you'd like to contribute, fork the repository, commit your changes to main branch 
and send a pull request.
Make sure you add yourself to authors.
