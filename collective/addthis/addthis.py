from zope.component import getUtility
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets import common
from zope.schema.interfaces import IVocabularyFactory


class AddThisViewlet(common.ViewletBase):
    """ AddThis viewlet """

    index = ViewPageTemplateFile('addthis.pt')

    @property
    def _settings(self):
        pprop = getToolByName(self.context, 'portal_properties')
        return pprop.addthis_properties

    @property
    def chicklets(self):
        vocab = getUtility(IVocabularyFactory, name="AddThis Social Media")
        results = [term for term in vocab(self.context)
                   if term.value in self._settings.addthis_chicklets]
        return results

    def getAddThisURL(self):
        """ Returns URL to AddThis service. If that isn't specified we'll return random URL I got from
        AddThis.com when this addon was developed. 
        """
        return self._settings.addthis_url or "http://www.addthis.com/bookmark.php?v=250&amp;username=xa-4b7fc6a9319846fd"
