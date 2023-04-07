from Pages.BasePage import BasePage
from Locators import model_details_locators as details_locators


class SupportedCommands(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_add_command(self):
        self.click_on_element(locator=details_locators.add_command)

    def get_command_by_name(self, locator: tuple) -> bool:
        element = self.get_element_by_locator(locator=locator)
        if element:
            return True
