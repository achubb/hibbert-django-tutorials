import dj_database_url
from settings import PROJECT_DIRECTORY 
from settings import SITE_ROOT
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

TEMPLATE_DEBUG = True

ADMINS = ()

MANAGERS = ADMINS


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Old Local Database Settings
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = { 'default': dj_database_url.config(
    default='sqlite:////%s/db.sqlite3' % PROJECT_DIRECTORY
    )         
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = ''

STATIC_URL = '/static/'

print os.path.join(PROJECT_DIRECTORY, 'static/')

STATICFILES_DIRS = (
       # os.path.join(PROJECT_DIRECTORY, 'static'),
       ('assets', os.path.join(PROJECT_DIRECTORY, 'static/')),
)

# Media - filesystem path to the directory that will hold user-uploaded files.

MEDIA_ROOT = os.path.join(PROJECT_DIRECTORY, 'static/')

MEDIA_URL = ''

AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

UPLOAD_FILE_PATTERN = "uploaded_files/%s_%s"
