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
    (r'^delete_people/$','address_book.views.delete_people'),
    (r'^change_people_list/$','address_book.views.change_people_list'),
    (r'^search_people/$','address_book.views.search_people'),
    url(r'^admin/', include(admin.site.urls)),

)
