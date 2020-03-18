import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


class challenge11(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("http://www.sling.com")
        self.assertIn("Sling TV", self.driver.title)
        self.urlVisited = set()
        self.urlAll = []

    def tearDown(self):
        self.driver.close()

    def test_challenge11(self):
        elements = self.driver.find_elements(By.XPATH, "//a")
        e_dict = dict()

        for e in elements:
            try:
                e_text = e.text
                e_dict[e_text] = e.get_attribute("href")
                self.urlAll.append(e_dict[e_text])
            except:
                print("There was error while getting attribute")

        print("\n\n############################################\n")
        print("       Here is the LIST with all urls       ")
        print("\n############################################\n")
        for l in self.urlAll:
            if l is not None:
                print(l)
                if l in self.urlVisited:
                    continue
                self.urlVisited.add(l)

        print("\n\n############################################\n")
        print("       Here is the SET with unique urls      ")
        print("\n############################################\n")
        for s in self.urlVisited:
            try:
                response = requests.request("GET", s)
                print(s + " - status code: " + str(response.status_code))
            except:
                print("Failed to go to the url: " + s)


if __name__ == '__main__':
    unittest.main()
