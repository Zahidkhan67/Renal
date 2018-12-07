from django.db import models
class Post(models.Model):
                        Username = models.CharField(max_length = 20)
                        Street = models.CharField(max_length = 20)
                        District = models.CharField(max_length = 20)
                        Phone =models.CharField(max_length = 18)
                       
                        def __str__(self):
                                    return 'Name = ' + self.Username + ' Address = '+ self.Street + ' District = ' +  self.District + ' Phone = ' + self.Phone +'\n'