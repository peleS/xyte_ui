xyte_ui
Testing Xyte ui with selenium test if 747 model exists in models

Using pytest and selenium in POM format I am assuming we are using Chrome
I am also assuming the Chrome version is 111_0_5563_64
Driver location is in Drivers
To run on windows set the "set_driver" fixture in conftest.py (under Tests) to chromedriver_112_0_5615_49.exe
To run on linux set the "set_driver" fixture in conftest.py (under Tests) to chromedriver_111_0_5563_64_linux

The structure is as follows :

Drivers : contains the driver files to run selenium from the repo
Locators : files containing all the needed locators per page , in this case the minimum required to answer the question
Pages : containing the Page objects (or the class to be used to create the page object)
Test_data : Any data we need to use for the different tests , in this case a single JSON file with the email and password
Tests : the actual test Classes , usually i would make sure the test classes correspond to a Page object
Utils : any tools or external functions to be used as "Helpers" not directly connected to Selenium or the Tests -
        In this case , a "read json" function under tools

A requirements.txt file for the module versions we are using (for an easy installation , especially with pycharm)

Note : Tests can also be divided into Page folders if there are too many


Install python : 3.8 or higher

install modules : from the requirements.txt file

set the working direcotry to : <Path to xyte Exercise Folder>\Tests

set the Target to script and the target path to : <Path to xyte Exercise Folder>\Tests

