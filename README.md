# ip_allocator
A django api service to manage IP address allocation to users.



Endpoint: /ip/allocate  
Method: POST  
Request Body:  
json
Copy code
{
    "customer_name": "John Doe",
    "email": "johndoe@email.com"
}  
Response:  
Status 201 for success, with allocated IP details.  
Status 400 for bad request.  
Status 500 if no IPs are available.



Endpoint: /ip/release/{ipAddress}
Method: PUT
Response:
Status 200 for success.
Status 404 if IP not found or not allocated.
List Allocated IPs



Endpoint: /ip/allocated
Method: GET
Response:
Status 200 with list of allocated IPs and associated customer details.
List Available IPs


Method: GET
Endpoint: /ip/available
Response:
Status 200 with a list of available IPs.

