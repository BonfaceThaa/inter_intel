import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

hotels = [
    {'id': 0,
     'hotel': 'Emara Hotel Ole Sereni',
     'rating': 4.5,
     'address': 18187,
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


@app.route('/api/v1/resources/hotels/all', methods=['GET'])
def api_all():
    '''
    function to serve data of all hotels
    :return: a JSON of attributed hotels
    '''
    return jsonify(hotels)


@app.route('/api/v1/resources/hotels', methods=['GET'])
def api_id():
    '''
    function to filter a hotel using id
    :return: a JSON of a single hotel and its attributes
    '''
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for hotel in hotels:
        if hotel['id'] == id:
            results.append(hotel)

    return jsonify(results)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
