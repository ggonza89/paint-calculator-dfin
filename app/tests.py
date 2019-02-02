import unittest
from paintCalculator import PaintCalculator

class TestPaintCalculator(unittest.TestCase):
    
    def test_calculateFeet_passSanitizedInput_returnsCorrectResult(self):
        sut = PaintCalculator()
        length = 5
        width = 5
        height = 5
        
        assert sut.calculate_feet(length, width, height) == 100

    def test_calculateGallonsRequired_returnsCorrectResultOfSurfaceAreaDividedBy400(self):
        sut = PaintCalculator()

        assert sut.calculate_gallons_required(700) == 2

    def test_calculateGallonsRequired_returnsResultRoundedUp(self):
        sut = PaintCalculator()

        assert sut.calculate_gallons_required(349) == 1

    def test_calculateRoomsData_formattedDataHasFeet(self):
        sut = PaintCalculator()
        formatted_data = {
            'length': 5,
            'width': 5,
            'height': 5
        }

        sut.calculate_each_rooms_data(formatted_data)

        assert 'ft' in formatted_data

    def test_calculateRoomsData_formattedDataHasGallons(self):
        sut = PaintCalculator()
        formatted_data = {
            'length': 5,
            'width': 5,
            'height': 5
        }

        sut.calculate_each_rooms_data(formatted_data)

        assert 'gallons' in formatted_data

    def test_calculateRoomsData_GallonsRequiredCorrectResult(self):
        sut = PaintCalculator()
        formatted_data = {
            'length': 5,
            'width': 5,
            'height': 5
        }

        sut.calculate_each_rooms_data(formatted_data)

        assert formatted_data['gallons'] == 1

    def test_calculateRoomsData_MultipleRooms_TotalGallonsCorrect(self):
        sut = PaintCalculator()
        all_data = [
            {
                'length': 5,
                'width': 5,
                'height': 5,
                'room': 1
            },
            {
                'length': 5,
                'width': 5,
                'height': 5,
                'room': 2
            }
        ]

        total_gallons_required = sut.calculate_rooms_data(all_data)

        assert total_gallons_required == 2

if __name__ == '__main__':
    unittest.main()
