from django.contrib import admin

# Register your models here.
from .models import BillingProfile, Card, Charge

admin.site.register(BillingProfile)

admin.site.register(Card)

admin.site.register(Charge)