# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope import schema
from collective.addthis import _
from plone.theme.interfaces import IDefaultPloneLayer


class IAddThis(Interface):
    """ AddThis marker """


class IAddThisControlPanel(Interface):
    """ AddThis Controlpanel"""


class IAddThisControlPanelForm(Interface):
    addthis_url = schema.URI(title=_(u"AddThis URL"), required=False,)
    addthis_script_url = schema.URI(title=_(u"AddThis JavaScript URL"), required=False,)

class IAddthisBrowserLayer(IDefaultPloneLayer):
    """Addthis marker
    """