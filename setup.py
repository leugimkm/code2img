#!/user/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="code2img",
    version="0.0.2",
    url="https://github.com/leugimkm/code2img",
    project_urls={
        "Documentation": "https://leugimkm.github.io/code2img/",
        "Tracker": "https://github.com/leugimkm/code2img/issues",
        "Source": "https://github.com/leugimkm/code2img",
    },
    license="MIT",
    author="leugimkm",
    author_email="leugimkm@systrien.com",
    description="Generate an image from source code (local or repository)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.7",
    classifiers=[
        "Environment :: Console",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        "console_scripts": [
            "code2img=code2img.__main__:main",
        ],
    },
)
