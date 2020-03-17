from django.db import models

# Create your models here.
class category(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=100)
    
    def __str__(self):
        return self.cname
class logo(models.Model):
    logoname = models.CharField(max_length=100)
    logoimage=models.ImageField(upload_to='upload/',default='mypic')
    category= models.ForeignKey(category, on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.logoname
    
class product(models.Model):
    pid= models.AutoField(primary_key=True)
    logoname= models.CharField(max_length=200)
    category= models.ForeignKey(category, on_delete=models.CASCADE)
    price= models.FloatField(max_length=1000,default=0.0)
    companyname=models.CharField(max_length=200)

    def __str__(self):
        return self.companyname