from django.db import models
from cloudinary.models import CloudinaryField


STATUS = (
        ('active','Active'),
        ('inactive','Inactive'),
    )

class Item(models.Model):

    STATUS_DICT = dict(STATUS)
    class Meta(object):
        db_table = 'item'

    status = models.CharField(
            'status', blank=False, default='inactive', max_length=50, db_index=True, choices=STATUS 
        )
    name = models.CharField(
        'Name', blank=False, null=False, max_length=50, db_index=True, default='Anonymous'
        )
    price = models.DecimalField(
        'price', blank=False, null=False, max_digits=14, decimal_places=2
        )
    image = CloudinaryField(
        'image', blank=True, null=True
        )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
        )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
        )

    def __str__(self):
        return self.name