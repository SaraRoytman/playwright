import re
from playwright.sync_api import expect, sync_playwright

def test_google_persistent():
    with sync_playwright() as p:
        
        browser = p.chromium.launch_persistent_context(
            user_data_dir="./my_profile", 
            headless=False,
            slow_mo=500
        )
        
        page = browser.new_page()
        page.goto("https://www.google.com/ncr")
        page.get_by_role("combobox", name="Search").fill("playwright python")
        page.keyboard.press("Enter")
        
        expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE), timeout=60000)
        browser.close()