from Pages.BasePage import BasePage


class SideBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_models(self, locator: tuple):
        self.click_on_element(locator=locator)

    # This should contain all the available selections on the side bar , for this interview i only implemented models
