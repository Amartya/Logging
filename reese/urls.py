from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'reese.views.home.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^reese/$', "reese.views.home.reeselog"),
    url(r'^admin/', include(admin.site.urls)),
)
