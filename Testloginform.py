from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import unittest
from Unittest_1 import Util

class TestScript05(unittest.TestCase):

    def setUp(self):
        binary = FirefoxBinary(Util.FIREFOX_PATH)
        profile = FirefoxProfile()
        self.driver = webdriver.Firefox()
        self.base_url = Util.BASE_URL
        self.driver.implicitly_wait(Util.WAIT_TIME)
        self.driver.get(self.base_url + "/V4/")

    def tearDown(self):
        self.driver.quit()

    def test_case05(self):
        for data in self.testData():
            username, password = data
            actual_title, actual_box_msg = self.login(username, password)
            self.verify_login(actual_title, actual_box_msg)

    def login(self, username, password):
        self.driver.find_element(By.NAME, "uid").clear()
        self.driver.find_element(By.NAME, "uid").send_keys(username)
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "btnLogin").click()

        try:
            alt = Alert(self.driver)
            actual_box_msg = alt.text
            alt.accept()
            return None, actual_box_msg
        except:
            page_text = self.driver.find_element(By.TAG_NAME, "tbody").text
            parts = page_text.split(Util.PATTERN)
            dynamic_text = parts[1]
            return dynamic_text, None

    def verify_login(self, actual_title, actual_box_msg):
        if actual_box_msg is not None:
            self.assertEqual(actual_box_msg, Util.EXPECT_ERROR)
        else:
            self.assertTrue(actual_title.startswith(Util.FIRST_PATTERN))
            self.assertRegex(actual_title[-4:], Util.SECOND_PATTERN)

    def testData(self):
        return [
            [Util.USER_NAME, Util.PASSWD],
            ["invalid", "valid"],
            ["valid", "invalid"],
            ["invalid", "invalid"]
        ]


if __name__ == '__main__':
    unittest.main()
