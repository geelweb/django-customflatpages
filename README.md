# django-customflatpages

![Build status](https://travis-ci.org/geelweb/django-customflatpages.svg?branch=master)

django-customflatpages extends the [Django flatpages app](https://docs.djangoproject.com/en/dev/ref/contrib/flatpages/) to add an
emplacement management.

## Requirements

 - Django 1.7 to 1.8
 - Pyhton 2.7 to 3.4

## Install

Using pip

    pip install https://github.com/geelweb/django-customflatpages/archive/0.3.3.zip

From source

    python setup.py install

## Configuring your Django installation

First you have to install the [Django flatpages app](https://docs.djangoproject.com/en/1.8/ref/contrib/flatpages/#installation).

Edit `settings.py` and add `'geelweb.django.customflatpages'` to the `INSTALLED_APPS`

Create the database tables using `python manage.py migrate`.

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

## Testing

Run unit-tests

    python tests/runtests.py
