from django.conf.urls import  url            #This is responsible for all url patterns thats url with start and end.
from . import views                                         #It goes to the views model and checks the function is defined there.
urlpatterns =[
                                  url(r'^$', views.contributions , name='contributions' ),                                         #if the url is www.x.com/contributions
]