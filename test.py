import pytest
import os
from selenium import webdriver
from common import locator as locator
from common import configuration as conf
from common import messages as message
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.google_page import GoogleSearchPage
from pages.flipkart_page import FlipkartPage

class TestFlikart:

    @pytest.fixture(autouse=True)
    def set_up(self, web_driver):
        """Test case run method according to testcase requirement.
        Parameters:
            web_driver: webdriver fixture for selenium
        Returns:
            None
        Raises:
            None
        """
        self.driver = web_driver
        self.wait = WebDriverWait(self.driver, 60)

        self.google_page = GoogleSearchPage(self.driver, locator, conf, message)
        self.flipkart_page = FlipkartPage(self.driver, locator, message)

    def test_flipkart_flow(self):
        """ Verify Flipkart shopping flow.
        Parameters:
            None
        Returns:
            None
        Raises:
            None
        """
        try:
            self.google_page.enter_google_search_text(message.FLIPKART_TEXT)
            self.google_page.display_google_search_suggestions()
            self.google_page.press_enter_from_google_search_textbox()
            self.google_page.click_on_flipkart_link()
            
            self.flipkart_page.close_login_popup()
            self.flipkart_page.navigate_window_air_conditioners_page()
            self.flipkart_page.select_add_compare_checkbox(2)
            self.flipkart_page.select_add_compare_checkbox(3)
            self.flipkart_page.select_add_compare_checkbox(6)
            self.flipkart_page.click_on_add_compare_button()
            
            # print item details
            self.flipkart_page.print_item_details(1)
            self.flipkart_page.print_item_details(2)
            self.flipkart_page.print_item_details(3)

            # get compare item page url and display avalibility
            self.compare_page_url = self.driver.current_url
            self.flipkart_page.add_to_cart(1)
            self.driver.get(self.compare_page_url)  
            self.flipkart_page.add_to_cart(2)
            self.driver.get(self.compare_page_url)
            self.flipkart_page.add_to_cart(3)
            self.flipkart_page.verify_avalibility_of_items_by_pincode(conf.PINCODE)

            print('------ Delivery details for {} pincode --------'.format(conf.PINCODE))
            self.flipkart_page.print_item_delivery_msg(1)
            self.flipkart_page.print_item_delivery_msg(2)
            self.flipkart_page.print_item_delivery_msg(3)

            self.flipkart_page.check_again_avalibility_of_items_by_pincode(conf.PINCODE2)

            print('------ Delivery details for {} pincode --------'.format(conf.PINCODE2))
            self.flipkart_page.print_item_delivery_msg(1)
            self.flipkart_page.print_item_delivery_msg(2)
            self.flipkart_page.print_item_delivery_msg(3) 
        except Exception as msg:
            print(str(msg))