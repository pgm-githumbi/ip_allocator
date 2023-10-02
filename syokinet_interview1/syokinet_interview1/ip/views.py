from django.shortcuts import render

# Create your views here.


# views.py in your 'ip' Django app

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
import json

@csrf_exempt  # Remove this decorator if CSRF protection is needed
def allocate_ip(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            customer_name = data.get('customer_name', None)
            email = data.get('email', None)
            customer, created = models.create_customer(
                customer_name=customer_name,
                customer_email=email
            )
            ip = models.allocate_ip(customer_email=email, customer=customer)
            if ip:
                response_data = {
                    'message': 'IP allocated successfully',
                    'customer_name': customer_name,
                    'email': email
                }
                return JsonResponse(response_data, status=200)
        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Invalid JSON in the request body'
            }, status=400)
        
        return JsonResponse({
            'error' : 'Could not allocate ip'
        }, status=400)

    return JsonResponse({'error': 'Unsupported HTTP method'}, status=405)

def release_ip(request, ip_address):
    try:
        released = models.release_ip(ip_address)
        if released:
            return JsonResponse({'message': f'IP address {ip_address} released successfully.'}, status=200)
    
    except Exception as e:
        return JsonResponse({
            'error': f'IP address {ip_address} not found or not allocated.',
            'exception' : f'Exception: {str(e)}',
        }, status=404)
    

import ipaddress




def insert_ip_addresses(request, number=100):
    def private_ipv4s():
        for network in ['10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16']:
            for ip in ipaddress.ip_network(network).hosts():
                yield ip

    i = 0
    for ip in private_ipv4s():
        if i >= number:
            return JsonResponse({'no_of_ips in db' : models.Ips.objects.count()},
                        status=200)
        models.Ips.objects.get_or_create(address=str(ip), defaults={})
        i += 1

    return JsonResponse({'no_of_ips in db' : models.Ips.objects.count()},
                        status=200)