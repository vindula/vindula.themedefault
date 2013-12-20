# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface

from plone.app.contentlisting.interfaces import IContentListing
from Products.CMFPlone.PloneBatch import Batch
from Products.PythonScripts.standard import url_quote_plus
from plone.app.search.browser import Search

from Products.CMFCore.utils import getToolByName

from vindula.myvindula.models.funcdetails import FuncDetails
from vindula.content.models.content import ModelsContent


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
        results_pessoas = []
        term_session = self.request.SESSION.get('SearchableText')
        tipo_busca_session = self.request.SESSION.get('facet.tipo')

        tipo_busca = self.request.form.get('facet.tipo', term_session)

        term = self.request.form.get('SearchableText', tipo_busca_session)

        if (not term_session and term) or (term_session != term):
            self.request.SESSION['SearchableText'] = term

        if (not tipo_busca_session and tipo_busca) or (tipo_busca_session != tipo_busca):
            self.request.SESSION['facet.tipo'] = tipo_busca

        if not query:
            query = {}

        if term:
            query = {'SearchableText': quote_bad_chars(term) + '*' }

        if tipo_busca == 'intranet':            
            results_pessoas = FuncDetails.get_AllFuncDetails(unicode(term, 'utf-8'))[:2]
            plone_utils = getToolByName(self.context, 'plone_utils')
            all_types = plone_utils.getUserFriendlyTypes([])
            
            #Removendo filtro de busca
            #Intranet deve buscar tudo
            #for i in ['Image','File', 'Servico']:
            #    all_types.remove(i)

            query['portal_type'] = all_types

        elif tipo_busca == 'pessoas':
            results = FuncDetails.get_AllFuncDetails(unicode(term, 'utf-8'))
            if batch:
                results = Batch(results, b_size, b_start)

            return results,[]

        elif tipo_busca == 'servico':
            query['portal_type'] = ['Servico']

        elif tipo_busca == 'biblioteca':
            query['portal_type'] = ['Image','File']
        
        
        if tipo_busca == 'structure':
            p_catalog = getToolByName(self.context, 'portal_catalog')
            query['portal_type'] = ['OrganizationalStructure']
            results_catalog = p_catalog(**query)
            
            UIDS=[]
            for item in results_catalog:
                UIDS.append(item.UID)
                
            data_structures = ModelsContent.getAllByContentType('OrganizationalStructure', True)
            for structure in data_structures:
                if structure.uid in UIDS:
                    UIDS.remove(structure.uid)
            
            result = [i for i in results_catalog if i.UID in UIDS]
            result = IContentListing(result)
            result = Batch(result, b_size, b_start)
        else:   
            result = super(SearchView,self).results(query=query,batch=batch,b_size=b_size, b_start=b_start)

        return result, results_pessoas


class UpdatedSearchView(grok.View, Search):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('vindula-livesearch_reply')

    def results(self, query=None, batch=True, b_size=10, b_start=0):
        results_pessoas = []
        _q_session = self.request.SESSION.get('_q')
        tipo_busca_session = self.request.SESSION.get('facet.tipo')

        _q = self.request.form.get('q', _q_session)
        tipo_busca = self.request.form.get('facet.tipo', tipo_busca_session)

        if (not _q_session and _q) or (_q_session != _q):
            self.request.SESSION['_q'] = _q

        if (not tipo_busca_session and tipo_busca) or (tipo_busca_session != tipo_busca):
            self.request.SESSION['facet.tipo'] = tipo_busca

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
            results_pessoas = FuncDetails.get_AllFuncDetails(unicode(_q, 'utf-8'))[:2]
            plone_utils = getToolByName(self.context, 'plone_utils')
            all_types = plone_utils.getUserFriendlyTypes([])
            
            #Removendo filtro de busca. 
            #Intranet deve buscar tudo
            #for i in ['Image','File', 'Servico']:
            #    all_types.remove(i)

            params['portal_type'] = all_types

        elif tipo_busca == 'pessoas':
            results = FuncDetails.get_AllFuncDetails(unicode(_q, 'utf-8'))
            if batch:
                results = Batch(results, b_size, b_start)

            return results,[]

        elif tipo_busca == 'servico':
            params['portal_type'] = ['Servico']

        elif tipo_busca == 'biblioteca':
            params['portal_type'] = ['Image','File']
            
        if tipo_busca == 'structure':
            p_catalog = getToolByName(self.context, 'portal_catalog')
            query['portal_type'] = ['OrganizationalStructure']
            results_catalog = p_catalog(**query)
            
            UIDS=[]
            for item in results_catalog:
                UIDS.append(item.UID)
                
            data_structures = ModelsContent.getAllByContentType('OrganizationalStructure', True)
            for structure in data_structures:
                if structure.uid in UIDS:
                    UIDS.remove(structure.uid)
            
            result = [i for i in results_catalog if i.UID in UIDS]
            result = IContentListing(result)
            result = Batch(result, b_size, b_start)
        else:   
            result = super(SearchView,self).results(query=query,batch=batch,b_size=b_size, b_start=b_start)

        params.update(query)

        return result, results_pessoas