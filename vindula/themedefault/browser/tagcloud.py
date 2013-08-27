# coding: utf-8
from Products.CMFPlone.utils import getToolByName
from plone.app.layout.navigation.root import getNavigationRoot
from Products.Five import BrowserView

class TagCloud(BrowserView):

    def calcTagSize(self, number, total, font_sizes):
#        base_count = 100.0/len(font_sizes)
#        number = (number*100)/total
#        count = base_count
#        for size in font_sizes:
#            if number <= count:
#               return size
#            count += base_count

        #TODO: Refazer a logica disso, eu fiz isso pois a antiga sempre retonava none quando fosse muitos objetos
        
        if (number >= 48):
            return 1.25
        elif (number >= 24):
            return 1
        else:
            return 0.75

    def getTags(self, limit=30):
        portal_url = getToolByName(self.context, 'portal_url')()
        tagOccs = self.getTagOccurrences()
        L = []
        # If count has been set sort by occurences and keep the "count" first

        total = 0
        #Range de tamanhos das tags
        sizes = [0.75,1,1.25]
        D = tagOccs

#        for result in tagOccs.get('result',[]):
#            if result.Subject:
#                subjects = result.Subject
#                total = total + 1
#                for subject in subjects:
#                    D[subject] = D.get(subject,0) + 1

        search_path = '/@@vindula-search?Subject='
        
        if D:
            D = sorted(D.items(), key=lambda t:t[1], reverse=1)[:limit]
            if total > limit:
                total = limit
            
            for tag_item in D:
                tag_name = tag_item[0]
                tag_qtd = tag_item[1]
                
                L.append((tag_name,self.calcTagSize(tag_qtd,total,sizes),search_path + tag_name))
            
            L.sort()
                
#        L = [ (tag_name,self.calcTagSize(D[tag_name],total, sizes),search_path + tag_name ) for tag_name in D.keys() ]
        return L



    def getSearchSubjects(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        result = list(catalog.uniqueValuesFor('Subject'))

        #result.sort()
        return result

    def getSearchTypes(self):
        putils = getToolByName(self.context, 'plone_utils')

        return putils.getUserFriendlyTypes()

    def getTagOccurrences(self):
        stats = {}
        catalog = getToolByName(self.context, 'portal_catalog')
        index = catalog._catalog.indexes['Subject']

        for key in index.uniqueValues():
            if key:
                t = index._index.get(key)
                if type(t) is not int:
                    stats[str(key)] = len(t)
                else:
                    stats[str(key)] = 1
        return stats
        
#        types = self.getSearchTypes()
#        tags = self.getSearchSubjects()
#        catalog = getToolByName(self.context, 'portal_catalog')
#        
#        tagOccs = {}
#        query = {}
#        L = []
#
#        # query['portal_type'] = ['Post','Author']
#
#        query['path'] = getNavigationRoot(self.context)
#
#        for tag in tags:
#            result = []
#
#            query['Subject'] = tag
#
#            result = catalog.searchResults(**query)
#            if result:
#                tagOccs[tag] = len(result)
#                for i in result:
#                    L.append(i)
#
#        tagOccs['result'] = L
#        return tagOccs
    
    def getTagSize(self, tagWeight, thresholds):
        size = 0
        if tagWeight:
            for t in thresholds:
                size += 1
                if tagWeight <= t:
                    break
        return size

    def getThresholds(self, sizes):
        """This algorithm was taken from Anders Pearson's blog:
         http://thraxil.com/users/anders/posts/2005/12/13/scaling-tag-clouds/
        """
        if not sizes:
            return [1 for i in range(0, 5)]
        minimum = min(sizes)
        maximum = max(sizes)
        return [pow(maximum - minimum + 1, float(i) / float(5))
            for i in range(0, 5)]