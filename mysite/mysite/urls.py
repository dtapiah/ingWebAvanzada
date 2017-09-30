from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^navegadorcito3/', include('navegadorcito3.urls')),
    url(r'^admin/', admin.site.urls),
]