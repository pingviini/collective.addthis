# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope import schema
from collective.addthis import _

class IAddThisControlPanel(Interface):
    """ AddThis Controlpanel"""

class IAddThisSettings(Interface):
    addthis_url = schema.URI(title=_(u"AddThis URL"), default="")
    