from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^$', 'home', name='homepage'),
    url(r'^(?P<post_id>[\d]+)-(?P<post_slug>[\w-]+)/$', 'post', name='post'),
)
