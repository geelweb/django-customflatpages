
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = [
    "django.contrib.sites",
    "django.contrib.flatpages",
    "geelweb.django.customflatpages",
]

SITE_ID = 1

SECRET_KEY = 'sfbysvgcizvncwhf89'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

FLATPAGES_EMPLACEMENTS = (
    ('footer', 'Flatpage with link in footer'),
    ('menu', 'Flatpage with link in menu'),
)

FLATPAGES_DEFAULT_EMPLACEMENT = 'footer'
