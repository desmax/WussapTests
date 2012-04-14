from django.conf.urls import patterns, url

urlpatterns = patterns('trains.views',
    url(r'^$', 'index'),
    url(r'^status/(?P<status_name>\w+)/$', 'status'),
    url(r'^view/(?P<train_id>\d+)/$', 'view'),
)