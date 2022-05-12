import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

# caps = Chrome().desired_capabilities.CHROME.copy()
# caps['acceptInsecureCerts'] = True
# driver = Chrome(desired_capabilities=caps)

#asi nutno spoustet i toto:
#chromedriver --url-base=/wd/hub 


print("jedu")
driver = Chrome()
driver.implicitly_wait(10)
driver.get("https://stackoverflow.com/questions/70230636/pytest-is-not-accessed-import-pytest-could-not-be-resolved-pylance")

print (driver.title)
print (driver.current_url)
driver.quit()

@pytest.fixture
def browser():
  yield driver
  driver.quit()