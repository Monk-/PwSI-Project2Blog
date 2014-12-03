
from django.conf.urls import *
from blog.views import *


urlpatterns = patterns ('',
   url(r'^$', all_users),

)