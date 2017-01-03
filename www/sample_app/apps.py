# -*- encoding: utf-8 -*-
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SampleAppConfig(AppConfig):
    name = 'sample_app'
    verbose_name = _('Sample App')

    label = 'sample_app'
