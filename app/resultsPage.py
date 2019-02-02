from basePage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class ResultsPage(BasePage):

    URL = "http://localhost:5000/results"

    def __init__(self, driver, dimensionsPage):
        self.dimensionsPage = dimensionsPage
        self.driver = driver

    def go_to_results_page(self, roomsData):
        self.dimensionsPage.go_to_dimensions_page(len(roomsData))

        for room in range(len(roomsData)):
            self.dimensionsPage.enter_length_input(room, roomsData[room]['length'])
            self.dimensionsPage.enter_width_input(room, roomsData[room]['width'])
            self.dimensionsPage.enter_height_input(room, roomsData[room]['height'])

        self.dimensionsPage.click_submit_button()

    def title_matches(self):
        """
        Verifies that hardcoded text appears in page title
        """
        return "Results!" == self.driver.title
    
    def is_header_matches(self):
        """
        Verifies that hardcoded header appears in page
        """
        return self.header_matches("Calculating Paint Required")

    def get_results_table_rows(self):
        """
        Gets the results table's rows
        """
        self.driver.implicitly_wait(1)
        return self.driver.find_elements_by_xpath("//table[@name='Results']//tr")

    def get_amount_columns(self):
        self.driver.implicitly_wait(1)
        return self.driver.find_elements_by_xpath("//table[@name='Results']//tr//td[starts-with(@name, 'amount')]")

    def get_gallon_columns(self):
        self.driver.implicitly_wait(1)
        return self.driver.find_elements_by_xpath("//table[@name='Results']//tr//td[starts-with(@name, 'gallons')]")

    def get_total_gallons_required(self):
        self.driver.implicitly_wait(1)
        return self.driver.find_element(*ResultsPageLocators.TOTAL_GALLONS_REQUIRED)

    def get_room_header(self):
        self.driver.implicitly_wait(1)
        return self.driver.find_element(*ResultsPageLocators.ROOM_HEADER)

    def get_amount_header(self):
        self.driver.implicitly_wait(1)
        return self.driver.find_element(*ResultsPageLocators.AMOUNT_HEADER)

    def get_gallon_header(self):
        self.driver.implicitly_wait(1)
        return self.driver.find_element(*ResultsPageLocators.GALLON_HEADER)

    def click_home_button(self):
        """
        Triggers the home button that navigates to home page
        """
        element = self.driver.find_element(*ResultsPageLocators.HOME_BUTTON)
        element.click()

class ResultsPageLocators:
    RESULTS_TABLE = (By.NAME, "Results")
    ROOM_HEADER = (By.NAME, "room-header")
    AMOUNT_HEADER = (By.NAME, "amount-header")
    GALLON_HEADER = (By.NAME, "gallons-header")
    HOME_BUTTON = (By.ID, "home")
    TOTAL_GALLONS_REQUIRED = (By.NAME, "total-gallons-required")
