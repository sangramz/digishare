from django.contrib import admin
from .models import Profile, Transactions, Earnings

# Register your models here.
admin.site.register(Profile)
admin.site.register(Transactions)
admin.site.register(Earnings)