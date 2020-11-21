# flipkart_Page:
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class FlipkartPage:
    """
    Flipkart page class to initialize the flipkart page object,
    that contain flipkart-page methods,
    to use it in test
    """
    def __init__(self, webdriver, locators, message):
        """Initialize the flipkart page common variables used across page
        Parameters:
            webdriver (instance): Instance of browser/selenium webdriver
            locators (instance): Instance of properties file contain constant
                                variable for locator
        Returns:
            None
        Raises:
            None
        """
        self.driver = webdriver
        self.wait = WebDriverWait(self.driver, 60)
        self.action = ActionChains(self.driver)
        self.locator = locators
        self.message = message

    def close_login_popup(self):
        """ Close login popup from page  and Verify it is not visible
        Parameters:
            None
        Returns:
            None
        Raises:
            None
        """
        if not self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator.FLIPKART_LOGIN_POPUP_CLOSE_BTN_BY_CSS))):
            raise ElementNotVisibleException('Unable to find Flipkart Log in page')
        else:
            print("Flipkart page Is Loaded successfully")
            self.login_popup_close_link = self.driver.find_element_by_css_selector(self.locator.FLIPKART_LOGIN_POPUP_CLOSE_BTN_BY_CSS)
            self.login_popup_close_link.click()
            self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, self.locator.FLIPKART_LOGIN_POPUP_CLOSE_BTN_BY_CSS)))
    
    def navigate_window_air_conditioners_page(self):
        """Navigate to "TV & Appliances - AirConditioners > Window AC’s" page is displayed
        Parameters:
            None
        Returns:
            None
        Raises:
            ElementNotVisibleException
        """
        if not self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.locator.FLIPKART_TVANDAPPLIANCE_LINK_BY_CSS))):
            raise ElementNotVisibleException('Unable to find "TV & Appliances - AirConditioners > Window AC’s" page.')
        else:
            self.tv_appliances_tab = self.driver.find_element_by_css_selector(self.locator.FLIPKART_TVANDAPPLIANCE_LINK_BY_CSS)
            self.action.move_to_element(self.tv_appliances_tab).perform()
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.locator.FLIPKART_WINDOWAC_LINK_BY_CSS)))
            self.window_ac_link = self.driver.find_element_by_css_selector(self.locator.FLIPKART_WINDOWAC_LINK_BY_CSS)
            self.action.move_to_element(self.window_ac_link).perform()
            self.window_ac_link.click()
    
    def select_add_compare_checkbox(self, item_no):
        """ Select add compare checkbox of item_no number of item
        Parameters:
            item_no: index of item from list of items
        Returns:
            None
        Raises:
            None
        """
        if not self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator.FLIPKART_WINDOWAC_ADD_COMPARE_CHECKBOX_BY_CSS))):
            raise ElementNotVisibleException('Unable to find add compare checkbox on Flipkart item list in page')
        else:
            self.add_compare_checkbox = self.driver.find_elements_by_css_selector(self.locator.FLIPKART_WINDOWAC_ADD_COMPARE_CHECKBOX_BY_CSS)
            self.add_compare_checkbox[item_no-1].click()
            print('Add item no {} to compare list'.format(item_no))
    
    def click_on_add_compare_button(self):
        """click on add compare button
            Parameters:
                None
            Returns:
                None
            Raises:
                None
        """
        if not self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator.FLIPKART_ADD_COMPARE_BTN_BY_CSS))):
            raise ElementNotVisibleException('Unable to find add compare checkbox on Flipkart item list in page')
        else:
            self.add_compare_btn = self.driver.find_element_by_css_selector(self.locator.FLIPKART_ADD_COMPARE_BTN_BY_CSS)
            self.add_compare_btn.click()
            print("clicked on add compare button")
            
    def print_item_details(self, item_no):
        """ Print item details of item_no number of item
        Parameters:
            item_no: index of item from list of items
        Returns:
            None
        Raises:
            None
        """
        if not self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator.FLIPKART_ADD_COMPARE_PAGE_ITEM_NAME_BY_CSS))):
            raise ElementNotVisibleException('Unable to find item details on Flipkart item add compare page')
        else:
            self.product_name = self.driver.find_elements_by_css_selector(self.locator.FLIPKART_ADD_COMPARE_PAGE_ITEM_NAME_BY_CSS)
            self.product_price = self.driver.find_elements_by_css_selector(self.locator.FLIPKART_ADD_COMPARE_PAGE_ITEM_PRICE_BY_CSS)
            print('Details of item no. {} is'.format(item_no))
            print('Name: ', self.product_name[item_no-1].text)
            print('Price: ', self.product_price[item_no-1].text)
    
    def add_to_cart(self, item_no):
        """ Add item to the cart
        Parameters:
            item_no:  index of item from list of items
        Returns:
            None
        Raises:
            None
        """
        if not self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator.FLIPKART_COMPARE_PAGE_ADD_TO_CART_BTN_BY_CSS))):
            raise ElementNotVisibleException('Unable to find add cart button on Flipkart item compare page')
        else:
            self.add_cart_element = self.driver.find_elements_by_css_selector(self.locator.FLIPKART_COMPARE_PAGE_ADD_TO_CART_BTN_BY_CSS)
            self.add_cart_element[item_no-1].click()
    
    def verify_avalibility_of_items_by_pincode(self, pincode):
        """ Verify availibility of item on specific pincode
        Parameters:
            pincode: pincode of address
        Returns:
            None
        Raises:
            None
        """
        if not self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator.DELIVERY_PINCODE_TXTBOX_BY_CSS))):
            raise ElementNotVisibleException('Unable to find text box to check avalability of item by pincode')
        else:
            self.pin_code_check_txtbox = self.driver.find_element_by_css_selector(self.locator.DELIVERY_PINCODE_TXTBOX_BY_CSS)
            self.pin_code_check_txtbox.clear()
            self.pin_code_check_txtbox.send_keys(pincode)

            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator.DELIVERY_PINCODE_TXTBOX_BY_CSS)))
            self.pin_code_check_txt = self.driver.find_element_by_css_selector(self.locator.DELIVERY_PINCODE_CHECK_BY_CSS)
            self.pin_code_check_txt.click()
    
    def print_item_delivery_msg(self, item_no):
        """ Print message of item delivery
        Parameters:
            item_no: index of item from list of items
        Returns:
            None
        Raises:
            None
        """
        if not self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator.FLIPKART_CART_PAGE_ITEM_NAME_BY_CSS))) or not self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator.DELIVERY_PINCODE_DROPDOWN_BY_CSS))):
            raise ElementNotVisibleException('Unable to find item details on Flipkart cart page')
        else:
            self.product_name = self.driver.find_elements_by_css_selector(self.locator.FLIPKART_CART_PAGE_ITEM_NAME_BY_CSS)
            self.product_delivery_details = self.driver.find_elements_by_css_selector(self.locator.DELIVERY_AVAILABLE_DETAILS_BY_CSS)
            print('Delivery details of item no. {} is'.format(item_no))
            print('Name: ', self.product_name[item_no-1].text)
            print('Delivery Details: ', self.product_delivery_details[item_no-1].text.split('|')[0])

    def check_again_avalibility_of_items_by_pincode(self, pincode):
        """ Verify availibility of item on specific pincode
        Parameters:
            pincode: pincode of address
        Returns:
            None
        Raises:
            None
        """
        if not self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator.DELIVERY_PINCODE_DROPDOWN_BY_CSS))):
            raise ElementNotVisibleException('Unable to find dropdown to check avalability of item by pincode')
        else:
            self.pin_code_check_dropdown = self.driver.find_element_by_css_selector(self.locator.DELIVERY_PINCODE_DROPDOWN_BY_CSS)
            self.pin_code_check_dropdown.click()
            self.verify_avalibility_of_items_by_pincode(pincode)