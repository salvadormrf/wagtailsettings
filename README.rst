(**Fork** of https://bitbucket.org/takeflight/wagtailsettings)

(Has some minor modifications)

===============
wagtailsettings 
===============

A plugin for Wagtail that provides add developer-defined settings to the admin.

Installing
==========

Install using pip::

    pip install wagtailsettings

It works with Wagtail 0.5 and upwards.

Add it to your ``INSTALLED_APPS``:

.. code:: python

    INSTALLED_APPS += [
        'wagtailsettings',
    ]


Using
=====

Create a model that inherits from ``BaseSetting``,
and register it using the ``register_setting`` decorator:

.. code:: python

    from wagtailsettings.models import BaseSetting, register_setting

    @register_setting
    class SocialMediaSettings(BaseSetting):
        facebook = models.URLField(
            help_text='Your Facebook page URL'
        )
        instagram = models.CharField(
            max_length=255, 
            help_text='Your Instagram username, without the @'
        )
        trip_advisor = models.URLField(
            help_text='Your Trip Advisor page URL'
        )
        youtube = models.URLField(
            help_text='Your YouTube channel or user account URL'
        )


A 'Settings' link will appear in the Wagtail admin,
with links to each of the settings models defined.

If access to a setting is required in the code,
the ``BaseSetting.for_site`` method will retrieve the setting for the supplied site:

.. code:: python

    def view(request):
        social_media_settings = SocialMediaSettings.for_site(request.site)
        ...
