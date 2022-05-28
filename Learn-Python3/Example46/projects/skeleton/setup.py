try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {"description": "This is an example project for Example 46 in Learn Python The Hard way.",
          "author": "Ulysses Carlos",
          "url": "There is no url for this module.",
          "download_url": "There is no place to download this.",
          "author_email": "ucarlos1@student.gsu.edu",
          "version": "0.1",
          "install_requires": ['nose'],
          "packages": ['Example46'],
          "scripts": [],
          "name": "Example46"}


setup(**config)
