from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# unittest is package for unit testing in Python
# this is by default included in Python
import unittest
# import time

class HomeTest(unittest.TestCase):

    # override method: setup
    def setUp(self):
        # this method is going to automatically execute 
        # before the tests start
        PATH="chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)

    def test_title(self):
        self.driver.get("http://54.144.197.133:5000/")
        # sleep(6)
        self.assertIn("Proper Title", self.driver.title)

    def test_link(self):
        self.driver.get("http://54.144.197.133:5000/")
        link = self.driver.find_element_by_link_text("link")
        link.send_keys(Keys.RETURN)
        self.assertIn("Query", self.driver.page_source)
        self.assertIn("no search results", self.driver.page_source)

if __name__ == "__main__":
    unittest.main()