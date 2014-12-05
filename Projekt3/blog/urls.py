from django.conf.urls import *
from blog.views import *

urlpatterns = patterns('',
                       url(r'^$', all_users),
                     #url(r'^register/', register),
                       url(r'^login', loginn),
                       url(r'^auth', auth_view),
                       url(r'^logout', logout_view),
                       url(r'^loggedin', loggedin),
                       url(r'^invalid', invalid_login),
                       url(r'^register', register_user),
                       url(r'^registration_success', register_success),
                       url(r'^profile/$', profile),

)