from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets import common


class AddThisViewlet(common.ViewletBase):
    """ AddThis viewlet """
    
    index = ViewPageTemplateFile('addthis.pt')

    def getAddThisURL(self):
        """ Returns URL to AddThis service. If that isn't specified we'll return random URL I got from
        AddThis.com when this addon was developed. 
        """
        
        pprop = getToolByName(self, 'portal_properties')
        addthis = pprop.addthis_properties
        
        return addthis.addthis_url or "http://www.addthis.com/bookmark.php?v=250&amp;username=xa-4b7fc6a9319846fd"