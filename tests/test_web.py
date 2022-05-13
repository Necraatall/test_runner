import pytest
import json
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

from selenium.webdriver import Chrome, Firefox

@pytest.fixture(scope='session')
def config():
  with open('tests/config.json') as config_file:
    data = json.load(config_file)
  return data

@pytest.fixture
def browser(config):
  # Initialize ChromeDriver
  if config['browser'] == 'chrome':
    driver = Chrome()
  elif config['browser'] == 'firefox':
    driver = Firefox()
  else:
    raise Exception(f'"{config["browser"]}" is not a supported browser')

  driver.implicitly_wait(config['wait_time'])
  # Return the driver object at the end of setup
  yield driver
  # For cleanup, quit the driver
  driver.quit()

def test_basic_duckduckgo_search(browser):
  # Set up test case data
  PHRASE = 'panda'

  # Search for the phrase
  search_page = DuckDuckGoSearchPage(browser)
  search_page.load()
  search_page.search(PHRASE)

  # Verify that results appear
  result_page = DuckDuckGoResultPage(browser)
  assert result_page.link_div_count() > 0
  assert result_page.phrase_result_count(PHRASE) > 0
  assert result_page.search_input_value() == PHRASE