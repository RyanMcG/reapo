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
from docopt import docopt, printable_usage
from fabric.colors import green, red
from fabric.api import env, run
from fabric.state import output
from fabric.network import disconnect_all
version = "0.1.0-SNAPSHOT"

usage_str = printable_usage(__doc__)

# Enable using hosts defined in ssh config.
env.use_ssh_config = True

# Set the default shell to be `sh` instead of `bash`.
env.shell = "/bin/sh -c"

output.commands = False


def display_error(e):
    print(red('ERROR: ', True) + e)
    print(usage_str)


def create_repo(repo_path):
    """Do it!"""
    res = run('uname -a', shell=False)
    return (res if res.failed else green, res)


def reapo(arguments):
    """Main function which delegates to fabric tasks."""
    host = arguments['<host>']
    if host:
        env.host_string = host
        (color, message) = create_repo(arguments['<repo>'])
        print(color(message))
    else:
        display_error("Host not specified!")
    disconnect_all()


def main():
    """Simply runs the script."""
    # Parse options based on docstring above. If it is the first usage then...
    arguments = docopt(__doc__, version=version)
    # continue by calling this function.
    reapo(arguments)

if __name__ == '__main__':
    main()
