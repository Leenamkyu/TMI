from django.db import models

# Create your models here.
class Companion(models.Model):
    objects = models.Manager()
    
    user = models.CharField(max_length = 200) #사용자 추가 - 새로추가
    status = models.CharField(max_length = 100, choices = (
        ('모집중','모집중'),
        ('모집완료','모집완료')
    )) 
    category = models.CharField(max_length = 100, choices = (
        ('음식','음식'),
        ('액티비티','액티비티'),
        ('관광','관광'),
        ('힐링','힐링')
    ))
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    country = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    bucket_list = models.CharField(max_length= 200)
    
    ###새로추가 8/9####
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    ##################


    body = models.TextField() 

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]