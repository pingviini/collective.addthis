from base import AddThisTestCase
from collective.addthis.interfaces import IAddThis
from collective.addthis.interfaces import IAddThisControlPanel


class TestProductInstall(AddThisTestCase):

    def afterSetUp(self):
        pass
        # self.types = ('InstantMessage',)


class TestInstantiation(AddThisTestCase):

    def afterSetUp(self):
        pass
        # Adding an InstantMessage anywhere - can only be done by a Manager or Portal Owner
        # self.setRoles(['Manager'])
        # self.portal.invokeFactory('InstantMessage', 'im1')

#    def testCreateInstantMessage(self):
#        self.failUnless('im1' in self.portal.objectIds())

#    def testInstantMessageInterface(self):
#        im = self.portal.im1
#        self.failUnless(IInstantMessage.providedBy(im))

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductInstall))
    suite.addTest(makeSuite(TestInstantiation))
    return suite