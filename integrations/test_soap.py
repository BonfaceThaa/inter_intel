from suds.client import Client

hello_client = Client('http://localhost:8888/?wsdl')

# print(hello_client.service.get_hotel(0))
print(hello_client.service.get_hotels())