import unittest
from selenium import webdriver
from dimensionsPage import DimensionsPage

class TestPaintCalculatorDimensionsPage(unittest.TestCase):
    
    def setUp(self):
        self.dimensionsPage = DimensionsPage(webdriver.Chrome())

    def tearDown(self):
        self.dimensionsPage.driver.close()

    def test_title_matches(self):
        assert self.dimensionsPage.title_matches()

    def test_header_matches(self):
        assert self.dimensionsPage.is_header_matches()

    def test_footer_matches(self):
        assert self.dimensionsPage.footer_matches()

    def test_sanitation_of_rooms_param(self):
        rooms = -1
        self.dimensionsPage.go_to_dimensions_page(rooms)
        dimensionsTableRows = self.dimensionsPage.get_dimensions_table_rows()
        assert 1 == len(dimensionsTableRows)

    def test_correct_number_of_rows_from_param(self):
        rooms = 500
        self.dimensionsPage.go_to_dimensions_page(rooms)
        dimensionsTableRows = self.dimensionsPage.get_dimensions_table_rows()
        assert rooms + 1 == len(dimensionsTableRows)
    
    def test_table_has_room_header(self):
        self.dimensionsPage.go_to_dimensions_page(1)
        assert self.dimensionsPage.get_room_header().text == "Room Number"

    def test_table_has_width_header(self):
        self.dimensionsPage.go_to_dimensions_page(1)
        assert self.dimensionsPage.get_width_header().text == "Width"

    def test_table_has_length_header(self):
        self.dimensionsPage.go_to_dimensions_page(1)
        assert self.dimensionsPage.get_length_header().text == "Length"
    
    def test_table_has_height_header(self):
        self.dimensionsPage.go_to_dimensions_page(1)
        assert self.dimensionsPage.get_height_header().text == "Height"

    def test_table_has_all_room_columns(self):
        rooms = 500
        self.dimensionsPage.go_to_dimensions_page(rooms)
        assert rooms == len(self.dimensionsPage.get_dimensions_table_room_columns())
    
    def test_table_has_all_length_columns(self):
        rooms = 500
        self.dimensionsPage.go_to_dimensions_page(rooms)
        assert rooms == len(self.dimensionsPage.get_dimensions_table_length_columns()), len(self.dimensionsPage.get_dimensions_table_length_columns())
    
    def test_table_has_all_width_columns(self):
        rooms = 500
        self.dimensionsPage.go_to_dimensions_page(rooms)
        assert rooms == len(self.dimensionsPage.get_dimensions_table_width_columns()), len(self.dimensionsPage.get_dimensions_table_width_columns())
    
    def test_table_has_all_height_columns(self):
        rooms = 500
        self.dimensionsPage.go_to_dimensions_page(rooms)
        assert rooms == len(self.dimensionsPage.get_dimensions_table_height_columns()), len(self.dimensionsPage.get_dimensions_table_height_columns())

    def test_no_inputs_submit_button_fails(self):
        self.dimensionsPage.go_to_dimensions_page(1)
        self.dimensionsPage.click_submit_button()
        assert self.dimensionsPage.redirect_did_not_occur()

    def test_invalid_length_input_submit_button_fails(self):
        self.dimensionsPage.go_to_dimensions_page(1)
        self.dimensionsPage.enter_length_input(0, "-1")
        self.dimensionsPage.click_submit_button()
        assert self.dimensionsPage.redirect_did_not_occur()

    def test_invalid_width_input_submit_button_fails(self):
        self.dimensionsPage.go_to_dimensions_page(1)
        self.dimensionsPage.enter_width_input(0, "-1")
        self.dimensionsPage.click_submit_button()
        assert self.dimensionsPage.redirect_did_not_occur()

    def test_invalid_height_input_submit_button_fails(self):
        self.dimensionsPage.go_to_dimensions_page(1)
        self.dimensionsPage.enter_height_input(0, "-1")
        self.dimensionsPage.click_submit_button()
        assert self.dimensionsPage.redirect_did_not_occur()

    def test_no_length_input_submit_button_fails(self):
        self.dimensionsPage.go_to_dimensions_page(1)
        self.dimensionsPage.enter_height_input(0, "1")
        self.dimensionsPage.enter_width_input(0, "1")
        self.dimensionsPage.click_submit_button()
        assert self.dimensionsPage.redirect_did_not_occur()

    def test_no_width_input_submit_button_fails(self):
        self.dimensionsPage.go_to_dimensions_page(1)
        self.dimensionsPage.enter_length_input(0, "1")
        self.dimensionsPage.enter_height_input(0, "1")
        self.dimensionsPage.click_submit_button()
        assert self.dimensionsPage.redirect_did_not_occur()

    def test_no_height_input_submit_button_fails(self):
        self.dimensionsPage.go_to_dimensions_page(1)
        self.dimensionsPage.enter_length_input(0, "1")
        self.dimensionsPage.enter_width_input(0, "1")
        self.dimensionsPage.click_submit_button()
        assert self.dimensionsPage.redirect_did_not_occur()

    def test_valid_inputs_submit_button_redirects_to_results_page(self):
        self.dimensionsPage.go_to_dimensions_page(1)
        self.dimensionsPage.enter_length_input(0, "1")
        self.dimensionsPage.enter_width_input(0, "1")
        self.dimensionsPage.enter_height_input(0, "1")
        self.dimensionsPage.click_submit_button()
        assert self.dimensionsPage.redirected_to_results_page()

if __name__ == '__main__':
    unittest.main()
