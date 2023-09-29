from django.shortcuts import render

# Create your views here.


# views.py in your 'ip' Django app

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Remove this decorator if CSRF protection is needed
def allocate_ip(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            customer_name = data.get('customer_name', '')
            email = data.get('email', '')
            # Process the data as needed
            # Here, we're just echoing the data back as a response
            response_data = {
                'message': 'IP allocated successfully',
                'customer_name': customer_name,
                'email': email
            }
            return JsonResponse(response_data, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in the request body'}, status=400)

    return JsonResponse({'error': 'Unsupported HTTP method'}, status=405)
