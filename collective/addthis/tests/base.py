import unittest

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
from Products.PloneTestCase.layer import onsetup

@onsetup
def setup_product():
    """Set up the package and its dependencies.
    
    The @onsetup decorator causes the execution of this body to be deferred
    until the setup of the Plone site testing layer. We could have created our
    own layer, but this is the easiest way for Plone integration tests.
    """
    
    fiveconfigure.debug_mode = True
    import collective.addthis
    zcml.load_config('configure.zcml', collective.addthis)
    fiveconfigure.debug_mode = False
        
    ztc.installPackage('collective.addthis')
    

setup_product()
ptc.setupPloneSite(products=['collective.addthis'])


class AddThisTestCase(ptc.PloneTestCase):
    """Base class for integration tests.

    This may provide specific set-up and tear-down operations, or provide
    convenience methods.
    """

class AddThisFunctionalTestCase(ptc.FunctionalTestCase):
    """We use this class for functional integration tests that use doctest
    syntax. Again, we can put basic common utility or setup code in here.
    """