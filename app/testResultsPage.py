import unittest
from resultsPage import ResultsPage
from dimensionsPage import DimensionsPage
from homePage import HomePage
from selenium import webdriver

class TestPaintCalculatorResultsPage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.resultsPage = ResultsPage(self.driver, DimensionsPage(self.driver))

    def tearDown(self):
        self.driver.close()

    def test_title_matches(self):
        roomsData = [
            {
                'length': 1,
                'width': 1,
                'height': 1
            }
        ]
        self.resultsPage.go_to_results_page(roomsData)
        assert self.resultsPage.title_matches()

    def test_header_matches(self):
        roomsData = [
            {
                'length': 1,
                'width': 1,
                'height': 1
            }
        ]
        self.resultsPage.go_to_results_page(roomsData)
        assert self.resultsPage.is_header_matches()
    
    def test_footer_matches(self):
        roomsData = [
            {
                'length': 1,
                'width': 1,
                'height': 1
            }
        ]
        self.resultsPage.go_to_results_page(roomsData)
        assert self.resultsPage.footer_matches()

    def test_table_headers_match(self):
        roomsData = [
            {
                'length': 1,
                'width': 1,
                'height': 1
            }
        ]
        self.resultsPage.go_to_results_page(roomsData)
        assert self.resultsPage.get_room_header().text == "Room #"
        assert self.resultsPage.get_amount_header().text == "Amount of Feet to Paint"
        assert self.resultsPage.get_gallon_header().text == "Gallons Required"

    def test_amount_of_feet_correct_per_row(self):
        roomsData = [
            {
                'length': 1,
                'width': 1,
                'height': 1,
                'amount': 4
            },
            {
                'length': 100,
                'width': 100,
                'height': 100,
                'amount': 40000
            }
        ]
        self.resultsPage.go_to_results_page(roomsData)
        amountColumns = self.resultsPage.get_amount_columns()
        for amountColumn in range(len(amountColumns)):
            assert str(roomsData[amountColumn]['amount']) == amountColumns[amountColumn].text, amountColumns[amountColumn].text

    def test_gallons_required_correct_per_row(self):
        roomsData = [
            {
                'length': 1,
                'width': 1,
                'height': 1,
                'gallons': 1
            },
            {
                'length': 100,
                'width': 100,
                'height': 100,
                'gallons': 100
            }
        ]
        self.resultsPage.go_to_results_page(roomsData)
        gallonColumns = self.resultsPage.get_gallon_columns()
        for gallonColumn in range(len(gallonColumns)):
            assert str(roomsData[gallonColumn]['gallons']) == gallonColumns[gallonColumn].text, gallonColumns[gallonColumn].text

    def test_total_gallons_required_correct(self):
        roomsData = [
            {
                'length': 1,
                'width': 1,
                'height': 1,
            },
            {
                'length': 100,
                'width': 100,
                'height': 100,
            }
        ]
        self.resultsPage.go_to_results_page(roomsData)
        assert "Total Gallons Required: 101" == self.resultsPage.get_total_gallons_required().text

    def test_home_button_redirects_to_home_page(self):
        roomsData = [
            {
                'length': 1,
                'width': 1,
                'height': 1,
            }
        ]
        self.resultsPage.go_to_results_page(roomsData)
        self.resultsPage.click_home_button()
        assert f"{HomePage.URL}?home=Home" == self.resultsPage.current_url()

    def test_multiple_rooms_multiple_rows_including_header(self):
        roomsData = []
        roomData = {
            'length': 1,
            'width': 1,
            'height': 1
        }
        for i in range(500):
            roomsData.append(roomData)
        self.resultsPage.go_to_results_page(roomsData)
        assert len(self.resultsPage.get_results_table_rows()) == 501

if __name__ == '__main__':
    unittest.main()
