from django.conf.urls import patterns, include, url
from django.contrib import admin
from iframe.urls import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'post.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('iframe.urls')),
)
