from Pages.BasePage import BasePage


class Models(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def find_model(self, locator) -> None:
        print('\nlooking for model in page\n')
        self.element_exists(locator)
