from Products.CMFCore.utils import getToolByName

def uninstall(portal, reinstall=False):
    """ Take care of uninstall and skip everything if we're reinstalling """

    if not reinstall:
        portal_properties = getToolByName(portal, "portal_properties")
        if 'addthis_properties' in portal_properties:
            portal_properties._delObject('addthis_properties')

        controlpanel = getToolByName(portal, 'portal_controlpanel')
        if 'setAddThisSettings' in [a.getId() for a in controlpanel.listActions()]:
            controlpanel.unregisterConfiglet('setAddThisSettings')    
    return "Ran all uninstall steps."