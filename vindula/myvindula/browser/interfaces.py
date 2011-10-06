from zope.interface import Interface

class IMyVindulaView(Interface):
    """ """
    def getPortrait():
        """ Return.... """

class IManagerUser(Interface):
    """ """
    def load_form():
        """ Return.... """

class IListUser(Interface):
    """ """
    def load_list():
        """ Return.... """
        
class IConfigUser(Interface):
    """ """
    def load_form():        
        """ Return.... """

class IMeusLinks(Interface):
    def get_meusLinks():
        """ Return.... """
