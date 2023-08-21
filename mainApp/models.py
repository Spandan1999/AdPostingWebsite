from django.db import models
from django.db import models
from django.contrib.auth.models import User


class AdPostModel(models.Model):
    AD_TYPES_CHOICES = [
        ('rent', 'Rent Ads'),
        ('sell', 'Sell Ads'),
        ('job', 'Job Ads'),
        ('commercial', 'Commercial Ads'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_type = models.CharField(max_length=20, choices=AD_TYPES_CHOICES)
    ad_title = models.CharField(max_length=100)
    ad_description = models.TextField()
    contact_info = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ad_title
