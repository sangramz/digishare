from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    phone       = models.IntegerField()
    avatar      = models.ImageField(upload_to='images/')
    address     = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.user.username} Profile'


class Transactions(models.Model):
    investor     = models.ForeignKey(Profile, on_delete=models.CASCADE)
    txnFrom      = models.CharField(max_length=50)
    txnAmount    = models.FloatField()
    txnCharge    = models.FloatField()
    txnType      = models.CharField(max_length=50)
    txnReason    = models.CharField(max_length=200)
    txnCreated   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.txnFrom
    

class Earnings(models.Model):
    pass


