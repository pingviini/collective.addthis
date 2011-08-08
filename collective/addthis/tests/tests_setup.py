from base import AddThisTestCase


class TestProductInstall(AddThisTestCase):

    def afterSetUp(self):
        pass
        # self.types = ('InstantMessage',)


class TestInstantiation(AddThisTestCase):

    def afterSetUp(self):
        self.default_url = "http://www.addthis.com/bookmark.php?v=250&username=xa-4b7fc6a9319846fd"
        self.default_script = "http://s7.addthis.com/js/250/addthis_widget.js#username=xa-4b7fc6a9319846fd"
        self.new_url = 'http://www.example.com'  
        pass

    def testAddThisProperties(self):
        """ Fail if we don't have addthis_properties inside portal_properties """
        self.failUnless('addthis_properties' in self.portal.portal_properties.objectIds())

    def testAddThisDefaultURLProperty(self):
        """ Fail unless we don't have default URL in addthis_url field """
        addthis_properties = self.portal.portal_properties.addthis_properties
        self.assertEquals(addthis_properties.addthis_url, self.default_url)

    def testAddThisDefaultScriptURLProperty(self):
        """ Fail unless we don't have default script URL in addthis_script_url field """
        addthis_properties = self.portal.portal_properties.addthis_properties
        self.assertEquals(addthis_properties.addthis_script_url, self.default_script)

    def testAddThisSetURL(self):
        addthis_properties = self.portal.portal_properties.addthis_properties
        addthis_properties.addthis_url = self.new_url
        self.assertEquals(addthis_properties.addthis_url, self.new_url)

    def testAddThisSetScriptURL(self):
        addthis_properties = self.portal.portal_properties.addthis_properties
        addthis_properties.addthis_script_url = self.new_url
        self.assertEquals(addthis_properties.addthis_script_url, self.new_url)

    def testAddThisCSSResources(self):
        portal_css = self.portal.portal_css
        self.failUnless('++resource++addthis.css' in portal_css.getResourcesDict().keys())

    def testAddThisJSResources(self):
        portal_javascripts = self.portal.portal_javascripts
        self.failUnless('++resource++addthis.js' in portal_javascripts.getResourcesDict().keys())


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductInstall))
    suite.addTest(makeSuite(TestInstantiation))
    return suite