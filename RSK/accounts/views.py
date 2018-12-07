# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, views as auth_views
from django.shortcuts import render, redirect
from django.contrib import messages                          #Messaging the template if something went wrong..
from django.conf import settings                            
from django.core.mail import send_mail

from .forms import SignUpForm
from .models import *
#from django.template.loader import get_template

def register(request):
            if request.method == 'POST':
                          if request.user.is_authenticated():
                                   messages.error(request, 'Error While Processing! Please Logout and Register Again, ' )
                                   return render(request, 'registration/register.html',   {}  )
                          form = SignUpForm(request.POST)
                          if form.is_valid():                                   
                              form.save()
                              userdetailModel = UserInformationDetails(
                                                                                                        username = request.POST.get('username'),
                                                                                                        phone = request.POST.get('phone'),
                                                                                                        address = request.POST.get('address'),
                                                                                                        email = request.POST.get('email'),
                                                                                                        password = request.POST.get('password1'),
                                                                                                        fullname = request.POST.get('fullname')
                                                                                                        ) 
                              userdetailModel.save()
                              username = form.cleaned_data.get('username')
                              raw_password = form.cleaned_data.get('password1')
                              
                              #EMAIL FACILIATING FEATURE...
                              name = request.POST.get('name')
                              email = request.POST.get('email')
                              subject = 'Contact Form Received.'
                              from_email = settings.DEFAULT_FROM_EMAIL
                              to_email = ['xahiidkhan@gmail.com']
                              send_mail(subject, "Hello World!", from_email, to_email, fail_silently =True )

                              #AFTER SAVE THE CURRENT FORM NOW LOGS THE UNAUTHENTICATED USER
                              user = authenticate(username=username, password=raw_password)
                              login(request, user)

                              #RETURNS THE HOMEPAGE LOG IN.
                              return redirect('Homepage')
            #Get Method =-> This gets execute when the page is loaded first time.
            else:                    
                        form = SignUpForm()                                                     #EMPTY FORM!
                        if request.user.is_authenticated():
                                   messages.error(request, 'Logged user cannot further register users. ' )
                                   return render(request, 'registration/register.html',   {   }  )
            return render(request, 'registration/register.html',   {  'form' : form }  )

###########################################################
#/*This fuction is responsible for keeping all the  background log details, it records all the login attempts happening on the website.
#/* It also includes any attempt thats is wrong username or password and show them in the admin panel.
def LoginLog(request):
            Attemptsuccess = False
            # name = request.POST.get('username')
            # raw_password = request.POST.get('password')
            # user = authenticate(username=name, password=raw_password)
            # login(request, user)
            if request.user.is_authenticated():
                                              Attemptsuccess = True
            logindetails = LogDetails(                      
                                      username = request.POST.get('username'),
                                      password = request.POST.get('password'),
                                      successful = Attemptsuccess
            )
            logindetails.save()
            return auth_views.login(request)


def wrapped_logi(request):
    if request.user.is_authenticated():
            return redirect('Homepage')
    else:
        return auth_views.login(request)