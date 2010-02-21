# -*- coding: utf-8 -*-

from zope.interface import implements
from zope.component import adapts
from zope.app.component.hooks import getSite

from plone.fieldsets.fieldsets import FormFields
from plone.app.controlpanel.form import ControlPanelForm

from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.utils import safe_hasattr
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import ProxyFieldProperty

from collective.addthis.interfaces import IAddThisControlPanelForm
from collective.addthis.interfaces import IAddThisControlPanel
from collective.addthis import _


class AddThisControlPanelAdapter(SchemaAdapterBase):
    
    adapts(IPloneSiteRoot)
    implements(IAddThisControlPanelForm)
    
    def __init__(self, context):
        super(AddThisControlPanelAdapter, self).__init__(context)
        self.portal = getSite()
        pprop = getToolByName(self.portal, 'portal_properties')
        self.context = pprop.addthis_properties

    addthis_url = ProxyFieldProperty(IAddThisControlPanelForm['addthis_url'])
    addthis_script_url = ProxyFieldProperty(IAddThisControlPanelForm['addthis_script_url'])

    def get_addthis_url(self):
        return getattr(self.context, 'addthis_url',
                       getattr(self.context, 'addthis_url', None))

    def set_addthis_url(self, value):
        if safe_hasattr(self.context, 'addthis_url'):
            self.context.addthis_url = value

    def get_addthis_script_url(self):
        return getattr(self.context, 'addthis_script_url',
                       getattr(self.context, 'addthis_script_url', None))

    def set_addthis_script_url(self, value):
        if safe_hasattr(self.context, 'addthis_script_url'):
            self.context.addthis_script_url = value
    
    ProxyFieldProperty(IAddThisControlPanelForm['addthis_url'])
    ProxyFieldProperty(IAddThisControlPanelForm['addthis_script_url'])


class AddThisControlPanel(ControlPanelForm):
    """ Pathkey control panel """
    
    implements(IAddThisControlPanel)

    form_fields = FormFields(IAddThisControlPanelForm)

    form_name = _(u"AddThis settings")
    label = _(u"AddThis settings")
    description = _(u"Here you can customize Addthis settings")