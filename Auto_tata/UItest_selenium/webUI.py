import unittest
from time import sleep

from selenium import webdriver


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

        # 窗口最大化
        self.driver.maximize_window()
        self.msg = '海贼王'
        self.url = 'http://www.baidu.com'

    def testSearch(self):
        """
        test body
        :return:
        """
        # open browser
        self.driver.get(self.url)
        sleep(2)
        # click search input
        self.driver.find_element_by_id('kw').click()
        sleep(2)

        # input value
        self.driver.find_element_by_id('kw').send_keys(self.msg)
        sleep(2)
        self.driver.find_element_by_id('su').click()
        sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
