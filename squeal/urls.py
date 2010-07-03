from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('razpilnik.squeal.views',
      (r'^$', 'index'),
      (r'^home/$', 'home'),
      (r'^(?P<squealer>\w+)/$', 'squealer'),
      (r'^(?P<squealer>\w+)/settings/$', 'settings')
)