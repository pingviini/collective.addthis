from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common


class AddThisViewlet(common.ViewletBase):
    """ AddThis viewlet """
    
    index = ViewPageTemplateFile('addthis.pt')

    def getAddThisURL(self):
        """ Returns URL to AddThis service """
        
        return "http://www.addthis.com/bookmark.php?v=250&amp;username=jyuplone"