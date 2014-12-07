from django.conf.urls import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from blog.views import *
from PSI import settings

urlpatterns = patterns('',
                       url(r'^$', index),
                     #url(r'^register/', register),
                       url(r'^login', loginn),
                       url(r'^auth', auth_view),
                       url(r'^logout', logout_view),
                       url(r'^loggedin', loggedin),
                       url(r'^invalid', invalid_login),
                       url(r'^register', register_user),
                       url(r'^registration_success', register_success),
                       url(r'^profile/$', profile),
                       url(r'^view/(?P<slug>[^\.]+).html', 'blog.views.view_post', name='view_blog_post'),
                       url(r'^category/(?P<slug>[^\.]+).html', 'blog.views.view_category', name='view_blog_category'),



)
