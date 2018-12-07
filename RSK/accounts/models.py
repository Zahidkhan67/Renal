# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import now

# To Add Changes..
#use "makemigration" with "python manage.py migrate --fake-initial"


class UserInformationDetails(models.Model):                                             #Don't delete this model ever... It cause an undetected bug.
                        username = models.CharField( max_length = 20 ,blank=True) 
                        fullname = models.CharField( max_length = 20 ,blank=True) 
                        address = models.CharField( max_length = 20 ,blank=True) 
                        phone =  models.CharField( max_length = 20 ,blank=True)
                        email =  models.EmailField( max_length = 40, blank=True)
                        password  =  models.CharField( max_length = 20,blank=True)
                        creationTime =  models.DateTimeField(auto_now_add = True)

                        def __str__(self):
                                    return self.username
#This model saves all the logs detail in background.
class LogDetails(models.Model):                                             #Don't delete this model ever... It cause an undetected bug.
                        username = models.CharField( max_length = 20 ,blank=True) 
                        password  =  models.CharField( max_length = 20,blank=True)
                        loginTime =  models.DateTimeField(default = now)
                        successful = models.BooleanField( default=False )

                        def __str__(self):
                                    return self.username 