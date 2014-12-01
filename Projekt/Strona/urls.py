from django.conf.urls import *
from Strona.views import archive
urlpatterns = patterns ('',
     url(r'^$', archive)
)
