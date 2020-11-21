from flask import Flask, jsonify, request
import typing

app = Flask(__name__)

my_persons: typing.List = []

@app.route('/persons', methods=['GET'])
def persons():
    """ Get all persons """

    return jsonify(my_persons)

@app.route('/persons', methods=['POST'])
def create_person():
    """ Add """

    # Check if all fields are available
    if request.json.get('street') and \
        request.json.get('number') and \
        request.json.get('postal_code'):
        my_persons.append(request.json)
    else:
        # Data is missing in the request
        return jsonify({"error": "Data incomplete"}), 400

    return jsonify(my_persons), 201

@app.route('/persons/<int:number>', methods=['GET'])
def person_number(number: int):
    """ Get the first person """
    person: typing.Dict = {}

    if len(my_persons) > number:
        person = my_persons[number]

    return jsonify(person)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)