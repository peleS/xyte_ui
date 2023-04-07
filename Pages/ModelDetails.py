from Pages.BasePage import BasePage
from Locators import model_details_locators as details_locators


class ModelDetails(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_supported_commands(self):
        self.click_on_element(locator=details_locators.commands)



