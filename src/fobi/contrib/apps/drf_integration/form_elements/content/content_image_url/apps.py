from django.apps import AppConfig

__title__ = 'fobi.contrib.apps.drf_integration.form_elements.content.' \
            'content_image_url.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2014-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)


class Config(AppConfig):
    """Config."""

    name = 'fobi.contrib.apps.drf_integration.form_elements.content.' \
           'content_image_url'
    label = 'fobi_contrib_apps_drf_integration_form_elements_content_' \
            'content_image_url'
