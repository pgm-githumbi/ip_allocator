from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)

class Ips(models.Model):
    AVAILABLE = 'available'
    ALLOCATED = 'allocated'
    RESERVED = 'reserved'
    STATUSES = ((AVAILABLE, AVAILABLE,), 
                (ALLOCATED, ALLOCATED), 
                (RESERVED, RESERVED))

    address = models.GenericIPAddressField()
    status = models.CharField(max_length=20, choices=STATUSES, 
                              default=AVAILABLE)
    customer = models.OneToOneField(Customer, null=True, default=None,
                                    on_delete=models.SET_NULL)
