# login_page.py
#
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class GoogleSearchPage:
    """
    Google Search page class to initialize the page object,
    that contain google-page methods,
    to use it in test
    """

    def __init__(self, webdriver, locators, conf, message):
        """Initialize the google page common variables used across page
        Parameters:
            webdriver (instance): Instance of browser/selenium webdriver
            locators (instance): Instance of properties file contain constant
                                variable for locator
            conf (instance): Instance of configuration file
            message (instance): Instance of WebPageMessageConstant file contain
                                constant message
        Returns:
            None
        Raises:
            None
        """
        self.driver = webdriver
        self.wait = WebDriverWait(self.driver, 60)
        self.locator = locators
        self.conf = conf
        self.message = message
    
    def enter_google_search_text(self, text):
        """ enter search text on google-page
            Parameters:
                text: text for google search
            Returns:
                None
            Raises:
                None
        """
        if self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.locator.GOOGLE_SEARCH_TEXTBOX_BY_CSS))):
            self.google_username_element = self.driver.find_element_by_css_selector(self.locator.GOOGLE_SEARCH_TEXTBOX_BY_CSS)
            self.google_username_element.clear()
            self.google_username_element.send_keys(text)
        else:
            print("Error while entering text on google search page")

    def display_google_search_suggestions(self):
        """display google search suggestions on google-search-page
            Parameters:
                None
            Returns:
                None
            Raises:
                None
        """
        if self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.locator.GOOGLE_SEARCH_SUGGESTIONS_BY_CSS))):
            self.suggestion_elements = self.driver.find_elements_by_css_selector(self.locator.GOOGLE_SEARCH_SUGGESTIONS_BY_CSS)
            print('----- Google Search Suggestions -----')
            for element in self.suggestion_elements:
                text = element.text
                print (text)
        else:
            print("Error while displaying google search content")

    def press_enter_from_google_search_textbox(self):
        """Press enter on google search textbox
            Parameters:
                None
            Returns:
                None
            Raises:
                None
        """
        if self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator.GOOGLE_SEARCH_TEXTBOX_BY_CSS))):
            self.driver.find_element_by_css_selector(self.locator.GOOGLE_SEARCH_TEXTBOX_BY_CSS).send_keys(Keys.ENTER)
        else:
            print("Error while searching text on google")

    def click_on_flipkart_link(self):
        """click on flipkart link to go to Flipkart website
            Parameters:
                None
            Returns:
                None
            Raises:
                None
        """
        if self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator.FLIPKART_LINK_BY_CSS))):
            self.flipkart_link = self.driver.find_element_by_css_selector(self.locator.FLIPKART_LINK_BY_CSS)
            self.flipkart_link.click()
            print("clicked on flipkart link")
        else:
            print("Error while click on flipkart link")