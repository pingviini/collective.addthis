# -*- coding: utf-8 -*-

from zope.interface import implements

from plone.fieldsets.fieldsets import FormFieldsets
from plone.app.controlpanel.form import ControlPanelForm

from collective.addthis.interfaces import IAddThisControlPanelForm
from collective.addthis.interfaces import IAddThisControlPanel

from collective.addthis import _


class AddThisControlPanel(ControlPanelForm):
    """ Pathkey control panel """
    
    implements(IAddThisControlPanel)

    addthis_configuration = FormFieldsets(IAddThisControlPanelForm)
    addthis_configuration.id = 'addthis_configuration'
    addthis_configuration.label = _(u"AddThis settings")

    form_fields = FormFieldsets(addthis_configuration)

    form_name = _(u"AddThis settings")
    label = _(u"AddThis settings")
    description = _(u"Here you can customize Addthis settings")