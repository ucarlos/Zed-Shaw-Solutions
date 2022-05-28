try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {"description": "My Project",
          "author": "Ulysses Carlos",
          "url": "URL to get the project.",
          "download_url": "Where to download it.",
          "author_email": "ucarlos1@student.gsu.edu",
          "version": "0.1",
          "install_requires": ['nose'],
          "packages": ['Example48'],
          "scripts": [],
          "name": "example48"}


setup(**config)
