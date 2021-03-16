# SOAP API
SOAP is an open-standard, XML-based messaging protocol for exchanging information among computers. The API was designed to work via internet while providing web services. A SOAP message is contains the following elements Envelop, Header, Body and Fault. 

## Overview
The example developed can be accessed from a Github account using this link. The project provides a simple API for retrieving a list of hotels in Nairobi and details of a particular hotel. This serves a simple purpose of allow users to explore hotels using the address, facilities and services provided and address.

## Spyne application
This example uses a simple wsgi webserver to deploy a web services using the SOAP API. The application is built using spyne version 2.9. A SOAP server application developed using Python.

## Creating the web application
The application is created using a Spyne Service that uses the `@srpc` decorator to expose methods for retrieving a list of hotels and retrieving a particular hotel. The decorator provides methods as remote procedure calls and define the data types that it accepts and returns. Spyne caters for the data types such as `Array`, `Integer` and `String` via the model module. The two methods provide for the functionality desired.  The `Hotel` class accommodates for complex objects and defines the hotel object. This class is used to create hotels from the hotels list using a for loop.

## Deploying the application
The defined service is exposed to the outside world using the HTTP protocol. The application server uses a wsgi server to serve the application as http server.

## Running the application
Run the application using the following command:
`python  soap_prot.py`

Testing the SOAP is done using the `soap_prot.py` file that utilizes the Suds Python library that is a SOAP client library. Suds can also be installed using pip. Basically, the script imports the client module that reads the WSDL file of the create endpoint at Running on http://localhost:8888/.  Using the client variable, the client uses the provided web services by injecting the required arguments. The get_hotel service expects an id that identifies a hotel and gives the following output:

On the other hand, the `get_hotels` service expects no arguments and returns a list hotels and their attributes. The output is shown below:


## Areas for improvement
The application is simple **POC** that demonstrates how SOAP API can be developed and utilized using Spyne. The following are areas of improvement:
1. Expand the methods (update and delete methods) of the Service class.
2. Store the data in a database.