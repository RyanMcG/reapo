"""Test reapo functionallity.

Uses pea as a simple BDD framework around nose to make testing nicer. To run
the tests use nose (and rednose if you want nice color):

    nosetests --rednose -v

"""
# Author: Ryan McGowan

# Modify import path to import current code.
import sys
import os
import doctest

from pea import step, TestCase, Given, When, Then, And, world
import reapo
from fabric.api import cd
from fabric.colors import yellow
from fabric.contrib.files import exists

doctest.ELLIPSIS_MARKER = '/*/'


# Given functions -------------------------------------------------------------

@step
def I_have_the_following_default_host(host):
    reapo.env.host_string = host


# When functions --------------------------------------------------------------

@step
def I_have_the_following_arguments(arg_str):
    """Use the given arguments for the rest of the story."""
    world.argv = arg_str.split()


@step
def I_parse_the_arguments():
    """Requres that world.argv is already set. Parses the arguments defined
    there with docopt."""
    world.arguments = reapo.docopt(reapo.__doc__, argv=world.argv,
                                   version=reapo.version)


@step
def I_execute():
    """Call the main reapo method on the parsed arguments."""
    reapo.reapo(world.arguments, False)


# Then functions --------------------------------------------------------------

@step
def A_git_repository_exists_at(repo_path, bare=False):
    """Ensure that a git repository was created at the given path."""
    world.assertTrue(exists(repo_path),
                     "Nothing exists at the given path (\"%s\")." % repo_path)
    with cd(repo_path):
        res = reapo.run('git config core.bare')
    world.assertTrue(res.succeeded)
    world.assertEqual(res, 'true' if bare else 'false')

# Test cases ------------------------------------------------------------------


class ReapoStories(TestCase):
    """Some test cases for reapo."""

    def setUp(self):
        """Setup ReapoStories tests."""
        super(ReapoStories, self).setUp()
        # Since this is testing we override output.commands to True.
        reapo.output.commands = True

    def tearDown(self):
        """Tear down ReapoStories."""
        super(ReapoStories, self).tearDown()
        reapo.disconnect_all()

    def test_doctest_works(self):
        """Run doctest against reapo."""
        try:
            doctest.testmod(reapo, verbose=False, raise_on_error=True)
        except doctest.DocTestFailure as failure:
            print(yellow("Tried (%s) in (\"%s\"):" % (failure.test.name,
                                                      failure.test.filename)))
            print(failure.example.source)
            print(yellow("Wanted:"))
            print(failure.example.want)
            print(yellow("Got:"))
            print(failure.got)
            world.fail("Doctest failed in %s (\"%s\" on line %d)" %
                       (failure.test.name, failure.test.filename,
                        failure.example.lineno))

    def test_creating_a_remote_repository(self):
        """Try creating a remote git repository (on localhost)."""
        Given.I_have_the_following_arguments('-v localhost derp')
        When.I_parse_the_arguments()
        And.I_execute()
        Then.A_git_repository_exists_at('derp', bare=True)
