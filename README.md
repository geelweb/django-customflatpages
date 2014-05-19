# django-customflatpages

django-customflatpages extends the django flatpages app
https://docs.djangoproject.com/en/dev/ref/contrib/flatpages/ to add an
emplacement management.

## Install

    git clone https://github.com/geelweb/django-customflatpages.git
    pip install django-customflatpages

syncdb

    python manage.py syncdb

or using south

    python manage.py migrate customflatpages

## Migrate

### from 0.1 to 0.2

Using south

    python manage.py migrate customflatpages

## Usage

In `settings.py` update the `INSTALLED_APPS

    INSTALLED_APPS = (
        ...
        'django.contrib.sites',
        'django.contrib.flatpages',
        'geelweb.fjango.customflatpages',
        ...
    )

Define the `FLATPAGES_EMPLACEMENTS` and `FLATPAGES_DEFAULT_EMPLACEMENT`

    FLATPAGES_EMPLACEMENTS = (
        ('footer', 'Flatpage with link in footer'),
        ('menu', 'Flatpage with link in menu'),
    )

    FLATPAGES_DEFAULT_EMPLACEMENT = 'footer'

In templates load the `customflatpages` tags

    {% load customflatpages %}

And use the `get_customflatpages` tag

    {% get_customflatpages at 'menu' as flatpages_menu %}

    <ul class="nav">
    {% for page in flatpages_menu %}
      <li><a href="{{ page.url }}">{{ page.title }}</a></li>
    {% endfor %}
