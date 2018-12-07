from django.conf.urls import  url
from .  import views
urlpatterns = [
                                                                        url(r'^$', views.patient , name = 'patients'),                                                                      #If the website is www.x.com/patients
                                                                        url(r'^submit/', views.register , name = 'submit'),                                                      #If the user submits the data in the fields of the form..
]
