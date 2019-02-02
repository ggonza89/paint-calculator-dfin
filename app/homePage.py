from basePage import BasePage
from dimensionsPage import DimensionsPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    URL = "http://localhost:5000/"

    def go_to_home_page(self):
        self.driver.get(HomePage.URL)

    def title_matches(self):
        """
        Verifies that hardcoded text appears in page title
        """
        return "Calculating Paint Amount" in self.driver.title

    def is_header_matches(self):
        """
        Verifies that hardcoded header appears in page
        """
        return self.header_matches("Calculating Paint Required")

    def form_label_matches(self):
        """
        Verifies that hardcoded text in form label appears in page
        """
        element = self.driver.find_element(*HomePageLocators.FORM_TITLE)
        return "Enter the number of rooms" in element.text

    def click_submit_button(self):
        """
        Triggers the submit button that navigates to dimensions page
        """
        element = self.driver.find_element(*HomePageLocators.SUBMIT_BUTTON)
        element.click()

    def enter_amount_of_rooms(self, rooms):
        """
        Enters room number into rooms input element
        """
        roomsInput = self.get_room_input()
        roomsInput.send_keys(rooms)

    def get_room_input(self):
        return self.driver.find_element(*HomePageLocators.ROOM_INPUT)

    def redirect_did_not_occur(self):
        return HomePage.URL == self.current_url()

    def redirected_to_dimensions_page(self, rooms):
        return f"{DimensionsPage.URL}?rooms={rooms}" in self.current_url()

class HomePageLocators:
    SUBMIT_BUTTON = (By.ID, "submit")
    ROOM_INPUT = (By.NAME, "rooms")
    FORM_TITLE = (By.CLASS_NAME, "lead")
