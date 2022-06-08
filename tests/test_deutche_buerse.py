from pages.result_value import DeutcheBuerseResultPage
from pages.search_value import DeutcheBuerseSearchPage


def test_basic_deutche_buerse_search(browser):
  # Set up test case data
  PHRASE = 'Deutsche Börse AG'

  # Search for the phrase
  search_page = DeutcheBuerseSearchPage(browser)
  search_page.load()
  #search_page.search(PHRASE)

  # Verify that results appear
  result_page = DeutcheBuerseResultPage(browser)
  assert result_page.link_div_count() > 0
  assert result_page.phrase_result_count(PHRASE) > 0
  assert result_page.search_input_value() == PHRASE

