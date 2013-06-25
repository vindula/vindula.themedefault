# coding: utf-8
from Products.CMFPlone.utils import getToolByName
from plone.app.layout.navigation.root import getNavigationRoot
from Products.Five import BrowserView

class TagCloud(BrowserView):

    def calcTagSize(self, number, total, font_sizes):
        base_count = 100.0/len(font_sizes)
        number = (number*100)/total
        count = base_count
        for size in font_sizes:
            if number <= count:
               return size
            count += base_count

    def getTags(self):
        portal_url = getToolByName(self.context, 'portal_url')()
        tagOccs = self.getTagOccurrences()
        # If count has been set sort by occurences and keep the "count" first

        total = 0
        #Range de tamanhos das tags
        sizes = [0.75,1,1.25]
        d = {}
        for result in tagOccs.get('result',[]):
            if result.Subject:
                subjects = result.Subject
                total = total + 1
                for subject in subjects:
                    d[subject] = d.get(subject,0) + 1

        search_path = '/@@vindula-search?Subject='

        L = [ (tag_name,self.calcTagSize(d[tag_name],total, sizes),search_path + tag_name ) for tag_name in d.keys() ]
        L.sort()
        return L



    def getSearchSubjects(self):
        catalog = getToolByName(self.context, 'portal_catalog')
        result = list(catalog.uniqueValuesFor('Subject'))

        #result.sort()
        return result

    def getSearchTypes(self):
        putils = getToolByName(self.context, 'plone_utils')

        return putils.getUserFriendlyTypes()

    def getTagOccurrences(self,):
        types = self.getSearchTypes()
        tags = self.getSearchSubjects()
        catalog = getToolByName(self.context, 'portal_catalog')

        tagOccs = {}
        query = {}
        L = []

        # query['portal_type'] = ['Post','Author']

        query['path'] = getNavigationRoot(self.context)

        for tag in tags:
            result = []

            query['Subject'] = tag

            result = catalog.searchResults(**query)
            if result:
                tagOccs[tag] = len(result)
                for i in result:
                    L.append(i)

        tagOccs['result'] = L
        return tagOccs

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


