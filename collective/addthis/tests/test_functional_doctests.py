import unittest
import doctest
import interlude

from Testing import ZopeTestCase as ztc

from collective.addthis.tests import base

def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    return unittest.TestSuite([

        ztc.ZopeDocFileSuite(
            'tests/functional.txt', package='collective.addthis',
            test_class=base.AddThisFunctionalTestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
            #globs=dict(interact=interlude.interact,)
            ),
            
        # We could add more doctest files here as well, by copying the file
        # block above.

        ])
