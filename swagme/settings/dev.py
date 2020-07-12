from .base import *

# SECURITY WARNING: don't run with debug turned on in production!


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'so6xa6qm1pne+x_&p-elc0yt9$z)%=@9j@u0@al@u48pypejcy'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SERVE_MEDIA_FILES = True
DEBUG = False

try:
    from .local import *
except ImportError:
    pass
