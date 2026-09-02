import re
from playwright.sync_api import expect

def test_googleSearch(page):
  page.goto("https://www.google.com/ncr") 

  try:
    page.get_by_role("button", name="accept all").click(timeout=3000)
  except:
    print("No popup")

  page.get_by_role("combobox", name="Search").fill("playwright python")






 
