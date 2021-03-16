# REST API
An API(Application Programming Interface) allows for information or functionality to be manipulated by other programs or even systems. A popular example is the WordPress REST API. In this case, REST stands for Representational State Transfer which is a way to implement web APIs. Such an API majorly runs on top of HTTP protocol and used JSON data. JSON is a data storage format designed to be easy to read and write. Generally, user’s require a starting place when working with a new API. This can be achieved by developing user-friendly URLS and a proper documentation of the various components of the API.

## Overview
The example developed can be accessed from a Github account using this link. The project provides a simple API for retrieving a list of hotels in Nairobi and details of a particular hotel. This serves a simple purpose of allow users to explore hotels using the address, facilities and services provided and address.


## Flask application
Flask is a web Framework developed using Python and is popular for simple and micro-service applications. The framework is built with simplicity in mind and gives a user the ability to develop simple or complex applications that can be extended using other features such as authentication and ORM. 

## Creating a web application
For this guide, you will need python 3.7, Flask 1.1.7 and a Python IDE. Create a folder to house the project(the location can be anywhere in your PC) and clone the sample application from Github. Create a virtual environment and use the requirements.txt file to install Flask which installs a few more dependencies. 

## Running the application
Change directory to the folder you created and run the application using the command below:
`python rest_prot.py`
If everything goes well the application will will have an output as illustrated below:
`Running on http://localhost:5000/ (Press CTRL+C to quit)`

Open your browser and type the following link http://127.0.0.1:8000/  to access the list of hotels endpoint. You should see a JSON output for the entries in the list object of the application. The jsonify function within Flask converts the list containing hotel dictionaries into a JSON object. The data is stored in memory and thus not persisted in a file or a database.  

For the case of a particular hotel of interest the user can use an id to filter out the hotel and get all the other attributes provided using this link http://localhost:8000/

## Areas of improvement
The application is simple POC that demonstrates how REST API can be developed and utilized using Flask. The following are areas of improvement:
1. Expand the available HTTP methods such as **PUT** and **DELETE**.
2. Store the data in a database
3. Use an ORM, serializer and deserializer to manipulate the data.
