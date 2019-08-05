from django.db import models

# Create your models here.
class Companion(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    country = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    bucket_list = models.CharField(max_length= 200)
    body = models.TextField()

    # user = models.CharField(max_length = 200) #사용자 추가 - 새로추가 

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]