#!/usr/bin/env python
# Author: Ryan McGowan
"""
A simple tool for creating remote repositories over ssh.

Usage:
  reapo [-v] [<repo>]
  reapo [-v] [<host>] <repo>
  reapo --help
  reapo --version

Options:
  -h --help     show this help message and exit
  -v --verbose  print additional information
  --version     print the version number
"""
from docopt import docopt
from fabric.colors import green, red
from fabric.api import env
version = "0.1.0-SNAPSHOT"


def create_repo(repo_path):
    return (False, "Oops!")


def reapo(arguments):
    """Main function which delegates to fabric tasks."""
    print(arguments)
    host = arguments['<host>']
    if host:
        env.hosts = host
        (success, message) = create_repo(arguments['<repo>'])
        color = green if success else red
        print(color(message))
    else:
        print(red("host not specified."))


def main():
    """Simply runs the script."""
    # Parse options based on docstring above. If it is the first usage then...
    arguments = docopt(__doc__, version=version)
    # continue by calling this function.
    reapo(arguments)

if __name__ == '__main__':
    main()
