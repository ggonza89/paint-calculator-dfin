import math

class PaintCalculator:

    def calculate_rooms_data(self, all_rooms_data):
        """
        Calculate the data for all rooms and return total gallons required
        :param all_rooms_data: list of room data
        :return: total gallons required
        """
        total_gallons_required = 0

        for room_data in all_rooms_data:
            self.calculate_each_rooms_data(room_data)
            total_gallons_required += room_data['gallons']

        return total_gallons_required

    def calculate_each_rooms_data(self, formatted_data):
        """
        Calculate rooms data required to paint the surface area of a single room
        and populate parameter passed in
        :param formatted_data: length width height data
        """
        feet = self.calculate_feet(formatted_data['length'], formatted_data['width'], formatted_data['height'])
        gallons = self.calculate_gallons_required(feet)
        formatted_data['ft'] = feet
        formatted_data['gallons'] = gallons

    def calculate_feet(self, length, width, height):
        """
        Calculate the number of feet required to paint the surface area of a single room
        :param length: length of room
        :param width: width of room
        :param height: height of room
        :return: integer for the number of feet required by performing `((Length * 2) + (Width * 2)) * Height`
        """
        return (int(length*2) + int(width*2)) * int(height)

    def calculate_gallons_required(self, feet):
        """
        Number of feet to paint divided by the amount of feet the paint will cover, rounded up
        :param feet: An integer for the number of feet required to paint
        :return: feet / paint coverage, rounded up
        """
        return math.ceil(feet / 400)
