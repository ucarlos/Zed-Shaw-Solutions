try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {"description": "Example 52 of Zed Shaw's Learn Python the Hard Way",
          "author": "Ulysses Carlos",
          "url": "N/A",
          "download_url": "N/A",
          "author_email": "ucarlos1@student.gsu.edu",
          "version": "0.1",
          "install_requires": ['nose'],
          "packages": ['gothonweb', "Example52"],
          "scripts": [],
          "name": "lpthw-example52"}


setup(**config)
