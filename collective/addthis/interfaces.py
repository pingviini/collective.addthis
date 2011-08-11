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
    """Control panel settings used to effect the rendering of the addthis
    viewlet."""

    addthis_url = schema.URI(title=_(u"AddThis URL"), required=False,)
    addthis_script_url = schema.URI(
        title=_(u"AddThis JavaScript URL"),
        required=False,
        )

    addthis_chicklets = schema.List(
        title=_(u"Social media selection"),
        description=_(u"A list of social media items that will be displayed "
                       "along side the share link as individual chicklets."),
        required=False,
        default=[],
        value_type=schema.Choice(title=_(u"Social media"),
                                 vocabulary="AddThis Social Media"),
        )


class IAddthisBrowserLayer(IDefaultPloneLayer):
    """Addthis marker"""


class ISocialMedia(Interface):
    """A source of listing of social media supported by the addthis service."""

    sources = schema.Iterable(
        title=_(u"social media sources"),
        description=_(u"A list of valid social media."),
        )
