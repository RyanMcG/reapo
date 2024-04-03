=====
reapo
=====
--------------------------------------------------------
A simple tool for creating remote repositories over ssh.
--------------------------------------------------------

Introduction
------------

*reapo* is a easy to configure tool for creating remote git repositories using
[Fabric](http://docs.fabfile.org/en/1.4.3/index.html). It's very simple.

Running *reapo* / Installation
----------------------------------

*reapo* is available via pip. ::

    pip install reapo

To install reapo from source: ::

    git clone git://github.com/RyanMcG/reapo.git
    cd reapo
    python setup.py install

If you want to run reapo from source you need to manually get the
dependencies first. ::

    # Assuming you are already in the Mr-Repo directory
    pip install -r requirements.txt

Usage
-----

Create a remote repository on your ssh host (myhost): ::

    reapo reap myhost:path/to/repo/you/are/creating
