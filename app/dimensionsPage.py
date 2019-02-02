from basePage import BasePage
from resultsPage import ResultsPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class DimensionsPage(BasePage):

    URL = "http://localhost:5000/dimensions"

    def go_to_dimensions_page(self, rooms):
        self.driver.get(f"{DimensionsPage.URL}?rooms={rooms}")
    
    def title_matches(self):
        """
        Verifies that hardcoded text appears in page title
        """
        self.go_to_dimensions_page(1)
        return "Dimension Calculation" in self.driver.title
    
    def is_header_matches(self):
        """
        Verifies that hardcoded header appears in page
        """
        self.go_to_dimensions_page(1)
        return self.header_matches("Calculating Paint Required")

    def get_dimensions_table(self):
        """
        Gets the dimensions table's element
        """
        self.driver.implicitly_wait(1)
        return self.driver.find_element(*DimensionsPageLocators.DIMENSIONS_TABLE)

    def get_dimensions_table_rows(self):
        """
        Gets the dimensions table's rows
        """
        self.driver.implicitly_wait(1)
        return self.driver.find_elements_by_xpath("//table[@name='dimensions_table']//tr")

    def get_room_header(self):
        self.driver.implicitly_wait(1)
        return self.driver.find_element(*DimensionsPageLocators.ROOM_HEADER)

    def get_length_header(self):
        self.driver.implicitly_wait(1)
        return self.driver.find_element(*DimensionsPageLocators.LENGTH_HEADER)

    def get_width_header(self):
        self.driver.implicitly_wait(1)
        return self.driver.find_element(*DimensionsPageLocators.WIDTH_HEADER)
    
    def get_height_header(self):
        self.driver.implicitly_wait(1)
        return self.driver.find_element(*DimensionsPageLocators.HEIGHT_HEADER)

    def get_dimensions_table_room_columns(self):
        """
        Gets the dimensions table's room columns
        """
        self.driver.implicitly_wait(1)
        return self.driver.find_elements_by_xpath("//table//tr//td[starts-with(@name, 'room')]")
    
    def get_dimensions_table_length_columns(self):
        """
        Gets the dimensions table's length columns
        """
        self.driver.implicitly_wait(1)
        return self.driver.find_elements_by_xpath("//table//tr//td//input[starts-with(@name, 'length')]")

    def get_dimensions_table_width_columns(self):
        """
        Gets the dimensions table's width columns
        """
        self.driver.implicitly_wait(1)
        return self.driver.find_elements_by_xpath("//table//tr//td//input[starts-with(@name, 'width')]")

    def get_dimensions_table_height_columns(self):
        """
        Gets the dimensions table's height columns
        """
        self.driver.implicitly_wait(1)
        return self.driver.find_elements_by_xpath("//table//tr//td//input[starts-with(@name, 'height')]")

    def click_submit_button(self):
        """
        Triggers the submit button that navigates to dimensions page
        """
        element = self.driver.find_element(*DimensionsPageLocators.SUBMIT_BUTTON)
        element.click()

    def redirect_did_not_occur(self):
        return DimensionsPage.URL in self.current_url()

    def redirected_to_results_page(self):
        return ResultsPage.URL in self.current_url()

    def enter_length_input(self, row, length):
        element = self.get_dimensions_table_length_columns()[row]
        element.send_keys(length)

    def enter_width_input(self, row, width):
        element = self.get_dimensions_table_width_columns()[row]
        element.send_keys(width)

    def enter_height_input(self, row, height):
        element = self.get_dimensions_table_height_columns()[row]
        element.send_keys(height)


class DimensionsPageLocators:
    DIMENSIONS_TABLE = (By.NAME, "dimensions_table")
    ROOM_HEADER = (By.NAME, "room-header")
    LENGTH_HEADER = (By.NAME, "length-header")
    WIDTH_HEADER = (By.NAME, "width-header")
    HEIGHT_HEADER = (By.NAME, "height-header")
    SUBMIT_BUTTON = (By.ID, "submit")
