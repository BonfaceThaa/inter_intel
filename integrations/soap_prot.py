
import logging

from spyne import Application, srpc, ServiceBase, String, Integer, Array
from spyne.protocol.soap import Soap11
from spyne.model.complex import ComplexModel
from spyne.server.wsgi import WsgiApplication

hotels_list = [
    {'id': 0,
     'hotel': 'Emara Hotel Ole Sereni',
     'rating': 4.5,
     'address': '18187',
     'features': ['free WiFi', 'free breakfast', 'free parking', 'wheelchair accessible', 'outdoor pool']},
    {'id': 1,
     'hotel': 'Eka Hotel',
     'rating': 4.5,
     'address': 'Mombasa Road, Nairobi',
     'features': ['free WiFi', 'free breakfast', 'free parking', 'wheelchair accessible', 'outdoor pool']},
    {'id': 2,
     'hotel': 'Panari Group',
     'rating': 4.3,
     'address': 'Panari Sky Center, Mombasa road, Nairobi',
     'features': ['free WiFi', 'breakfast', 'free parking', 'wheelchair accessible', 'indoor pool']},
    {'id': 3,
     'hotel': 'The Boma Nairobi',
     'rating': 4.5,
     'address': 'Cross rd, Nairbi',
     'features': ['free WiFi', 'paid breakfast', 'free parking', 'laundry service', 'outdoor pool']},
]

hotels = {}


class Hotel(ComplexModel):
    __namespace__ = "hotel"

    id = Integer
    hotel = String
    rating = String
    address = String


for i,v in enumerate(hotels_list):
    hotels[i] = Hotel(
        id=v['id'],
        hotel=v['hotel'],
        rating=str(v['rating']),
        address=v['address']
    )


class HotelService(ServiceBase):
    @srpc(Integer, _returns=Hotel)
    def get_hotel(hotel_id):
        '''
        get a single hotel
        :param hotel_id: id of a hotel
        :return: hotel with provided id
        '''
        return hotels[hotel_id]

    @srpc(_returns=Array(Hotel))
    def get_hotels():
        '''
        function to get the list of hotels
        :return: an array of hotel values
        '''
        global hotels

        return hotels.values()


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    application = Application([HotelService],
                              'spyne.examples.hello.http',
                              in_protocol=Soap11(validator='lxml'),
                              out_protocol=Soap11()
                              )

    wsgi_application = WsgiApplication(application)

    server = make_server('localhost', 8888, wsgi_application)

    logging.info("listening to http://127.0.0.1:8888")
    logging.info("wsdl is at: http://localhost:8888/?wsdl")

    server.serve_forever()
