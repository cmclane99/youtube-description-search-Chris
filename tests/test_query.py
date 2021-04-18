from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# unittest is package for unit testing in Python
# this is by default included in Python
import unittest
# import time

class QueryTest(unittest.TestCase):

    # override method: setup
    def setUp(self):
        # this method is going to automatically execute 
        # before the tests start
        PATH="chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)

    def test_query_in_url(self):
        driver = self.driver
        driver.get("http://54.144.197.133:5000/query?q=hiking")
        result_list = driver.find_elements_by_class_name("youtube-video")
        self.assertEqual(len(result_list), 100)
        self.assertIn("hiking", result_list[0].get_attribute('innerHTML'))

        #### test the search bar
        search_box = driver.find_element_by_name("description_search")
        search_box.send_keys("gear")
        search_button = driver.find_element_by_name("search_button")
        search_button.click()
        result_list = driver.find_elements_by_class_name("youtube-video")
        self.assertGreaterEqual(len(result_list), 1)
        self.assertIn("gear", result_list[0].get_attribute('innerHTML'))

if __name__ == "__main__":
    unittest.main()