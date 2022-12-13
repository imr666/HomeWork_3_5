import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def browser_manager():
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.quit()
