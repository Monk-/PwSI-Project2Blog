from django.conf.urls import patterns, include, url
from django.contrib import admin
import blog.urls
from PSI import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/', include(blog.urls)),
    url(r'^profile_images/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT})
)
handler500 = "blog.views.handler500"
handler404 = "blog.views.handler404"
handler403 = "blog.views.handler403"
handler401 = "blog.views.handler401"
handler400 = "blog.views.handler400"

