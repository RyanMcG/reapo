#from distutils.core import setup
from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as \
        description_file:
    long_description = description_file.read()
with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as \
        requirements_file:
    requirements = [line.rstrip() for line in requirements_file]


setup(name='reapo',
      version='0.1.0-SNAPSHOT',
      author='Ryan McGowan',
      author_email='ryan@ryanmcg.com',
      description="A simple tool for creating remote repositories over ssh.",
      long_description=long_description,
      url='https://github.com/RyanMcG/reapo',
      install_requires=requirements,
      entry_points={
          'console_scripts': [
              'reapo = reapo:main'
          ]
      },
      classifiers=['Development Status :: 4 - Beta',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3']
      )
