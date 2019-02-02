from flask import Flask, render_template, request
import math
from paintCalculator import PaintCalculator

app = Flask(__name__)

@app.route('/')
def index():
    """
    Loads the index page
    :return: Index page
    """
    return render_template("index.html")


@app.route('/dimensions', methods=['GET'])
def dimensions():
    """
    Sanitizes inputs from the first page and displays the Dimensions page
    :return: Dimensions page
    """
    rooms = sanitize_input(request.args.get("rooms"))
    return render_template("dimensions.html", rooms=rooms)


@app.route('/results', methods=['POST'])
def results():
    """
    Performs most of the logic for paint calculations
    :return: Results page
    """
    data = request.values
    number_of_data_sets = len(data) / 3
    all_data = []
    paintCalc = PaintCalculator()

    for room_number in range(int(number_of_data_sets)):
        formatted_data = extract_rooms_info(data, room_number)
        all_data.append(formatted_data)

    total_gallons_required = paintCalc.calculate_rooms_data(all_data)

    return render_template("results.html", all_data=all_data, total_gallons_required=total_gallons_required)


def sanitize_input(input):
    """
    This universe doesn't allow for negative numbers of rooms or feet
    :param input: Any number
    :return: The absolute, integer number
    """
    return abs(int(input))


def extract_rooms_info(data, room_number):
    """
    Sanitizes inputs, and then constructs a dict of the room information
    :param data: User input for LWH of a room
    :param room_number: The number of the room that is being processed
    :return: A formatted dict with room information
    """
    formatted_data = {'length': sanitize_input(data.get("length-%d" % room_number)),
                      'width': sanitize_input(data.get("width-%d" % room_number)),
                      'height': sanitize_input(data.get("height-%d" % room_number)),
                      'room': room_number + 1
                      }
    return formatted_data


# Boiler plate for starting the application
if __name__ == '__main__':
    app.run()
