from django.db import models
from investors import models as investorsModels

# Create your models here.
class InvestmentPlans(models.Model):
    propTitle           = models.CharField(max_length=100)
    propDescription     = models.CharField(max_length=700)
    propDetails         = models.CharField(max_length=500)
    propLocation        = models.CharField(max_length=100)
    propImage           = models.ImageField(upload_to='images/')
    amount              = models.FloatField()
    minInvest           = models.FloatField()
    maxInvest           = models.FloatField()
    returnRate          = models.CharField(max_length=50)
    capital             = models.CharField(max_length=50)

    def __str__(self):
        return self.propTitle


class Investments(models.Model):
    user                = models.ForeignKey(investorsModels.Profile, on_delete=models.CASCADE)
    propInvested        = models.ForeignKey(InvestmentPlans, on_delete=models.CASCADE)
    amount              = models.FloatField()
    investDate          = models.DateTimeField(auto_now_add=True)


    
    
   
