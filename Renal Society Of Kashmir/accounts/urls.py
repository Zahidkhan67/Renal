from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[

                        url(r'^register/$', views.register, name='register'),
                        url(r'^register/submit$', views.register ),
                        url(r'^logout/$', auth_views.logout, {'next_page' : 'Homepage'}, name='logout'),
                        url(r'^login/$', views.wrapped_logi, name='login'),
                        url(r'^login/attempt/$', views.LoginLog, name='LogFileFirst'),
                        url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--

]