from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://cgi-lib.berkeley.edu/ex/fup.html')
    page.set_input_files('input[type=file]', '안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕하세요안녕,HELLO_WORLD,하세요안녕하세요안,HELLO_WORLD,녕하세요안녕하세요안녕하세요.txt')
    page.locator('input[type=submit]').click()
    assert "file's contents are" in page.text_content('body')
