from zope.i18nmessageid import MessageFactory
import os

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('vindula.myvindula')

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))