from selenium.webdriver.common.by import By


class DeutcheBuerseSearchPage:
  URL = 'https://deutsche-boerse.com/dbg-en/'

  SEARCH_INPUT = (By.TARGET, '_boersefrankfurt')

  def __init__(self, browser):
    self.browser = browser

  def load(self):
    self.browser.get(self.URL)

  def search(self, phrase):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    #search_input.send_keys(phrase + Keys.RETURN)
    