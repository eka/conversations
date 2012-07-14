from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'conv.views.home', name='home'),
    # url(r'^conv/', include('conv.foo.urls')),
    url(r'(?P<cid>\d+)/$', 'conversations.views.conversation_get', name='conversation'),
    url(r'^$', 'conversations.views.conversation_list', name='conversations'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
