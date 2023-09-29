from django.db import IntegrityError, models, transaction
from django.forms import ValidationError

# Create your models here.


class Customer(models.Model):
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    customer_email = models.EmailField(max_length=255, unique=True)

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
    

def create_customer(customer_name, customer_email):
    names = customer_name.split(' ')
    fname = names[0]
    if len(names) >= 2:
        lname = names[-1]
    else:
        lname = ''
    try:
        cust, created = Customer.objects.get_or_create(
            customer_first_name=fname, customer_last_name=lname, 
            customer_email=customer_email
        )
    except IntegrityError as e:
        return None, False
    except ValidationError as e:
        return None, False
    
    return cust, created
    

def allocate_ip(customer_email=None, customer_first_name=None, 
                customer_last_name=None, customer_id=None,
                customer=None):
    if customer_email is not None:
        customer = Customer.objects.get(email=customer_email)
    elif customer_id is not None:
        customer = Customer.objects.get(pk=customer_id)
    elif customer is not None:
        kwargs = {'customer_first_name' : customer_first_name,
                  'customer_last_name' : customer_last_name}
        for key in kwargs:
            if kwargs[key] is None:
                kwargs.pop(key)
        if (customer_count := Customer.objects.filter(**kwargs).count()) > 1:
            raise ValueError("Too vague, more than one customer returned")
        customer = Customer.objects.filter(**kwargs).first()

    if customer is None:
        raise ValueError("Customer not found")
    
    try:
        with transaction.atomic():
            # Find the first available IP address (assuming you have a field `is_allocated` to track allocation status)
            ip_to_allocate = Ips.objects.filter(
                status=Ips.AVAILABLE
            ).first()

            if ip_to_allocate is None:
                return None # No available IP
            
            # Update the customer field for the allocated IP address
            ip_to_allocate.customer = customer
            ip_to_allocate.status = Ips.ALLOCATED
            ip_to_allocate.save()
            return ip_to_allocate
            

    except Exception as e:
        # Handle exceptions if the allocation fails
        print(f"An error occurred while allocating an IP address: {e}")
        return None
    




    
    
    
