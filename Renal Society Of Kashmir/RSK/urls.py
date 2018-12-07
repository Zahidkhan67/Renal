from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
            url(r'^admin/', include(admin.site.urls)),
            url(r'^home/', include('homepage.urls')),
            url(r'^patients/', include('patient.urls')),
            url(r'^contributions/', include('contributions.urls')),
            url(r'^donate/', include('donate.urls')),
            
            #The accounts contain the django accounts management url as well Programmer urls
            url(r'^accounts/', include('accounts.urls')),
            url(r'^accounts/', include('django.contrib.auth.urls')),
]
