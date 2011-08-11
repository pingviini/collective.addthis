# -*- coding: utf-8 -*-
import json
from urllib import urlopen
from zope.interface import implements, alsoProvides
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from collective.addthis.interfaces import ISocialMedia

SHARING = "http://cache.addthiscdn.com/services/v1/sharing.en.json"


class SocialMediaSources(object):
    """Provides a list of Social Media supported by the addthis.com service."""
    implements(ISocialMedia)

    def _services(self):
        """Returns the services using that addthis API"""
        response = urlopen(SHARING)
        data = json.load(response)
        # FIXME Error handling?
        return data[u'data']

    @property
    def sources(self):
        for service in self._services():
            try:
                unicode(service[u'name'], 'utf-8')
            except TypeError:
                value = service[u'name'].encode('ascii', 'ignore')
                service[u'name'] = unicode(value)
            yield (service[u'name'], service[u'code'],)
        raise StopIteration


def socialMediaVocabulary(context):
    """Vocabulary factory for social media sources."""
    utility = getUtility(ISocialMedia)
    terms = [SimpleTerm(value, token, token)
             for token, value in utility.sources]
    return SimpleVocabulary(terms)

alsoProvides(socialMediaVocabulary, IVocabularyFactory)
