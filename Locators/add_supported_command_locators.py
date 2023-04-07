from selenium.webdriver.common.by import By

name = (By.CSS_SELECTOR, "input[name='friendly_name']")
description = (By.CSS_SELECTOR, "input[name='description']")
name_on_device = (By.CSS_SELECTOR, "input[name='name']")
create_button = (By.XPATH,
                 '//button[contains(@class,"mantine-Button-root") and @data-button="true"]/div/span[text()="Create"]')

supported_command_error = (By.XPATH, "//div[@class='rrt-title'][contains(text(), 'Add supported command error')]")
