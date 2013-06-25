# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface

from Products.CMFPlone.PloneBatch import Batch
from Products.PythonScripts.standard import url_quote_plus
from plone.app.search.browser import Search

from Products.CMFCore.utils import getToolByName

from vindula.myvindula.models.funcdetails import FuncDetails

grok.templatedir('templates')

def quotestring(s):
    return '"%s"' % s

def quote_bad_chars(s):
    bad_chars = ["(", ")"]
    for char in bad_chars:
        s = s.replace(char, quotestring(char))
    return s

multispace = u'\u3000'.encode('utf-8')

class SearchView(grok.View, Search):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('vindula-search')

    def results(self, query=None, batch=True, b_size=10, b_start=0):
        tipo_busca = self.request.form.pop('tipo', '')
        term = self.request.form.get('SearchableText', '')

        if not query:
            query = {}

        if term:
            query = {'SearchableText': quote_bad_chars(term) + '*' }

        if tipo_busca == 'intranet':

            plone_utils = getToolByName(self.context, 'plone_utils')
            all_types = plone_utils.getUserFriendlyTypes([])
            for i in ['Image','File', 'Servico']:
                all_types.remove(i)

            query['portal_type'] = all_types


        elif tipo_busca == 'pessoas':

            results = FuncDetails.get_AllFuncDetails(unicode(term, 'utf-8'))
            if batch:
                results = Batch(results, b_size, b_start)

            return results


        elif tipo_busca == 'servico':
            query['portal_type'] = ['Servico']

        elif tipo_busca == 'biblioteca':
            query['portal_type'] = ['Image','File']

        # import pdb;pdb.set_trace()
        print query

        return super(SearchView,self).results(query=query,batch=batch,b_size=b_size, b_start=b_start)





class UpdatedSearchView(grok.View,  Search):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('vindula-livesearch_reply')


    def results(self, query=None, batch=True, b_size=10, b_start=0):
        _q = self.request.form.get('q', '')
        tipo_busca = self.request.form.get('tipo', '')
        #

        if not query:
            query = {}

        for char in ('?', '-', '+', '*', multispace):
            _q = _q.replace(char, ' ')

        r = _q.split()
        r = " AND ".join(r)
        r = quote_bad_chars(r) + '*'
        searchterms = url_quote_plus(r)


        params = {'SearchableText': r }

        if tipo_busca == 'intranet':

            plone_utils = getToolByName(self.context, 'plone_utils')
            all_types = plone_utils.getUserFriendlyTypes([])
            for i in ['Image','File', 'Servico']:
                all_types.remove(i)

            params['portal_type'] = all_types


        elif tipo_busca == 'pessoas':
            results = FuncDetails.get_AllFuncDetails(unicode(_q, 'utf-8'))
            if batch:
                results = Batch(results, b_size, b_start)

            return results


        elif tipo_busca == 'servico':
            params['portal_type'] = ['Servico']

        elif tipo_busca == 'biblioteca':
            params['portal_type'] = ['Image','File']


        params.update(query)

        return super(UpdatedSearchView,self).results(query=params,batch=batch,b_size=b_size, b_start=b_start)



