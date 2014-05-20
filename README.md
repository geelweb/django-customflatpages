# django-customflatpages

django-customflatpages extends the django flatpages app
https://docs.djangoproject.com/en/dev/ref/contrib/flatpages/ to add an
emplacement management.

## Install

Using pip

    pip install https://github.com/geelweb/django-customflatpages/archive/0.2.zip

From source

    python setup.py install

## Configuring your Django installation

Edit `settings.py` and add `'geelweb.django.customflatpages'` to the `INSTALLED_APPS`

Create the database tables using `python manage.py syncdb` or `python manage.py migrate customflatpages` if your application use [south](http://south.aeracode.org/)

If your application use [south](http://south.aeracode.org/), and you try to upgrade from django-customflatpages 0.1 to 0.2, you have to execute `python manage.py migrate customflatpages 0001 --fake` before the migrate command.

## Configuring django-customflatpages

Define the `FLATPAGES_EMPLACEMENTS` and `FLATPAGES_DEFAULT_EMPLACEMENT` in
settings

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

