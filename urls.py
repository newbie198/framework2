# -*- coding: utf-8 -*-
"""
urls config
"""
from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()
from django.conf import settings
# 公共URL配置
urlpatterns = patterns(
    '',
url(r'^','home_application.views.index'),
)


handler404 = 'error_pages.views.error_404'
handler500 = 'error_pages.views.error_500'
handler403 = 'error_pages.views.error_403'
handler401 = 'error_pages.views.error_401'
