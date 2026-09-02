import re
from playwright.sync_api import Page, expect


def test_googleSearch(page: Page):

  page.wait_for_timeout(3000)
  page.goto("https://www.google.com/ncr") 

  try:
    page.get_by_role("button", name="accept all").click(timeout=3000)
  except:
    print("No popup")

  page.get_by_role("combobox", name="Search").fill("playwright python")
  page.keyboard.press("Enter")

  
  expect(page).to_have_title(re.compile("playwright", re.IGNORECASE))
  page.pause()
  






 
