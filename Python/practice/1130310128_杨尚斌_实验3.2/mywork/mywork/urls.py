#from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mywork.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#)
#from django.conf.urls.defaults import * 
from django.conf.urls import *

urlpatterns = patterns('',
    (r'^addr_book/$','address_book.views.addr_book'),
    (r'^people_list/$','address_book.views.people_list'),
)
