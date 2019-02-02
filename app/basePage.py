class BasePage(object):
    """
    Base class to initialize the base page that will be called from all pages
    """

    def __init__(self, driver):
        self.driver = driver

    def header_matches(self, header):
        element = self.driver.find_element_by_name("page-header")
        return header in element.text

    def footer_matches(self):
        elements = self.driver.find_elements_by_xpath("//footer/p")
        matches = element[0].text == "1 gallon of paint is required for every 400ft of surface."
        matches &= element[1].text == "The surface area to paint is"
        matches &= element[2].text == "Gallons required will be rounded up."
        return matches

    def current_url(self):
        return self.driver.current_url
