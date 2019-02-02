import unittest
from selenium import webdriver
from homePage import HomePage

class TestPaintCalculatorHomePage(unittest.TestCase):

    def setUp(self):
        self.homePage = HomePage(webdriver.Chrome())
        self.homePage.go_to_home_page()

    def tearDown(self):
        self.homePage.driver.close()

    def test_title_matches(self):
        assert self.homePage.title_matches()

    def test_header_matches(self):
        assert self.homePage.is_header_matches()

    def test_footer_matches(self):
        assert self.homePage.footer_matches()
    
    def test_form_label_matches(self):
        assert self.homePage.form_label_matches()

    def test_invalid_room_input_submit_button_fails(self):
        self.homePage.enter_amount_of_rooms("-1")
        self.homePage.click_submit_button()
        assert self.homePage.redirect_did_not_occur()

    def test_no_room_input_submit_button_fails(self):
        self.homePage.click_submit_button()
        assert self.homePage.redirect_did_not_occur()
    
    def test_submitButton_redirectsTo_dimensionsPage(self):
        rooms = "1"
        self.homePage.enter_amount_of_rooms(rooms)
        self.homePage.click_submit_button()
        assert self.homePage.redirected_to_dimensions_page(rooms)

if __name__ == '__main__':
    unittest.main()
