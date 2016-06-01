from base import *

DEBUG = True

INSTALLED_APPS = INSTALLED_APPS + (
    'behave_django', 'debug_toolbar')

# Behave settings
SPLINTER_DRIVER = os.environ.get('SPLINTER_DRIVER', 'phantomjs')
