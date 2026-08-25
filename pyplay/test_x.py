import re
from playwright.sync_api import expect, Page

def test_google(page: Page):
    
    page.goto("https://www.google.com/ncr")

    page.get_by_role("combobox", name = "Search").fill("playwright python")

    page.keyboard.press("Enter")

    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))
    
    page.wait_for_timeout(10000)





  
