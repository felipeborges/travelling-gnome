from django.conf.urls import patterns, include, url

urlpatterns = patterns('events.views',
    url(r'(?P<event_slug>\w+)/(?P<year>\d{4})/$', 'event_page'),
)