from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'superdudes.app.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup-email/', 'superdudes.app.views.signup_email'),
    url(r'^email-sent/', 'superdudes.app.views.validation_sent'),
    url(r'^login/$', 'superdudes.app.views.home'),
    url(r'^logout/$', 'superdudes.app.views.logout'),
    url(r'^done/$', 'superdudes.app.views.done', name='done'),
    url(r'^app/$', 'superdudes.app.views.app', name='app'),
    url(r'^email/$', 'superdudes.app.views.require_email', name='require_email'),
    url(r'', include('social.apps.django_app.urls', namespace='social'))
)
