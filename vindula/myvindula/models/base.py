from zope.component import getUtility
from storm.zope.interfaces import IZStorm
from storm.locals import Store

class BaseStore(object):
   
    def __init__(self, *args, **kwargs):
        self.store = getUtility(IZStorm).get('myvindula')
        
        # inicializacao preguicosa do objeto
        for attribute, value in kwargs.items():
            if not hasattr(self, attribute):
                
                raise TypeError('unexpected argument %s' % attribute)
            else:
                setattr(self, attribute, value)
            