from playwright.sync_api import sync_playwright

class Crawler:

    def __init__(self):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=False)
        self.page = self.browser.new_page()
    
    def goto(self, url):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def close(self):
        self.browser.close()
        self.p.stop()

    def find(self, selector):
        return self.page.query_selector_all(selector)
    
    def wait_for_load(self, state="networkidle"):
        self.page.wait_for_load_state(state)