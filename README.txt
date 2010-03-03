Introduction
============

*collective.addthis* is a simple Plone addon which brings `addthis.com`_ 
services to Plone pages under document actions.

*collective.addthis* has customizable addthis url (pointing to your addthis
username) and addthis javascript url (pointing to addthis javascript url).
Those settings have default values which I got from `addthis.com`_ so that testing
collective.addthis is easy. Those values are recommended to be changed if you're
actually planning to use this addon.

There are few other similar addons for Plone (`collective.prettysociable`_,
`collective.plonebookmarklets`_, `sc.social.bookmarks`_) which does the same job,
but they were too much customized to some direction to suit some specific needs.
New `collective.sharerizer`_ is closest relative to *collective.addthis*. Differences
between these two are that collective.sharerizer overrides document_actions where
collective.addthis is placed under them in it's own viewlet.

.. _addthis.com: http://www.addthis.com 
.. _collective.prettysociable: http://plone.org/products/collective.prettysociable
.. _collective.plonebookmarklets: http://plone.org/products/plonebookmarklets
.. _sc.social.bookmarks: http://plone.org/products/sc.social.bookmarks
.. _collective.sharerizer: http://plone.org/products/collective.sharerizer
