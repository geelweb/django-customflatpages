# django-customflatpages

django-customflatpages extends the [Django flatpages app](https://docs.djangoproject.com/en/dev/ref/contrib/flatpages/) to add an
emplacement management.

## Install

Using pip

    pip install https://github.com/geelweb/django-customflatpages/archive/0.2.zip

From source

    python setup.py install

## Configuring your Django installation

First you have to install the [Django flatpages app](https://docs.djangoproject.com/en/1.6/ref/contrib/flatpages/#installation).

Edit `settings.py` and add `'geelweb.django.customflatpages'` to the `INSTALLED_APPS`

Create the database tables using `python manage.py syncdb` or `python manage.py migrate customflatpages` if your application use [south](http://south.aeracode.org/)

If your application use [south](http://south.aeracode.org/), and you try to upgrade from django-customflatpages 0.1 to 0.2, you have to execute `python manage.py migrate customflatpages 0001 --fake` before the migrate command.

## Settings

**FLATPAGES_EMPLACEMENTS**

Default: () (Empty tuple)

A tuple that lists flatpages emplacements. Each item of the tuple must be a
tuple of ('code', 'Human readable name') Example :

    FLATPAGES_EMPLACEMENTS = (
        ('footer', 'Flatpage with link in footer'),
        ('menu', 'Flatpage with link in menu'),
    )

**FLATPAGES_DEFAULT_EMPLACEMENT**

Default: None

The code of the flatpages default emplacement. Exemple:

    FLATPAGES_DEFAULT_EMPLACEMENT = 'footer'

## Getting a list of flatpages in your templates

django-customflatpages app provides a template tag that allow you to iterate
over all of the available flatpages. The `get_customflatpages` implement the
`get_flatpages` feature and allow you to

 * [display registration required flatpages](https://docs.djangoproject.com/en/1.6/ref/contrib/flatpages/#displaying-registration-required-flatpages)
 * [limit flatpages by base URL](https://docs.djangoproject.com/en/1.6/ref/contrib/flatpages/#limiting-flatpages-by-base-url)

in addition `get_customflatpages` adds the following features

**Limiting flatpages by emplacement**

The `at 'emplacement_code'` option allow to filter flatpages on the defined
emplacement.

For example:

    {% load customflatpages %}
    {% get_customflatpages at 'menu' as flatpages_menu %}
    <ul class="nav">
        {% for page in flatpages_menu %}
            <li><a href="{{ page.url }}">{{ page.title }}</a></li>
        {% endfor %}
    </ul>

