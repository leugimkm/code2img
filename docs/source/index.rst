.. code2img documentation master file, created by
   sphinx-quickstart on Wed Mar 23 01:35:52 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to code2img's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

::

                 _     ___ _           
       ___ ___ _| |___|_  |_|_____ ___ 
      |  _| . | . | -_|  _| |     | . |
      |___|___|___|___|___|_|_|_|_|_  |
                                  |___|



` code2img` is a simple tool to generate an image from a local file or
from a GitHub repository. It can also be used to send the source code
to carbon.now.sh and generate the image there.

Installation
============

`code2img` is available on `PyPi <https://pypi.org/project/code2img/>`_ (MIT license)
and installation can be performed by running `pip <https://docs.python.org/es/3/installing/index.html>`_

.. code-block:: console

   python -m pip install code2img

To upgrade the package:

.. code-block:: console

   python -m pip install code2img --upgrade

To delete the package:

.. code-block:: console

   python -m pip uninstall code2img


Example
=======

To generate an image from a local file:

.. code-block:: console

   > python -m code2img main.py -s
   Done!
   Image created in current directory: main.png 

To generate an image from a GitHub repository:

.. code-block:: console

   > python -m code2img soluciones/fibonacci.py -g
   Done!
   Image created in current directory: fibonacci.png

You can also send the content of the source code to carbon.now.sh:

.. code-block:: console

   > python -m code2img main.py -c
   Sent to Carbon.now.sh

   > python -m code2img soluciones/fibonacci.py -gc
   Sent to Carbon.now.sh

Help command:

.. code-block:: console

   > code2img -h

or:

.. code-block:: console

   > code2img --help


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
