from playwright.sync_api import sync_playwright

class Crawler:

    def __init__(self):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch_persistent_context(
            user_data_dir="./user_data",
            headless=False
        )
        self.page = self.browser.new_page()
        self.browser.pages[0].close()  # Close the default blank page
    
    def goto(self, url):
        self.page.goto(url)
        self.wait_for_load()

    def close(self):
        self.browser.close()
        self.p.stop()

    def find(self, selector):
        return self.page.query_selector_all(selector)
    
    def wait_for_load(self, state="load"):
        self.page.wait_for_load_state(state)

    def get_url(self):
        return self.page.url
    
    def expect_navigation(self):
        return self.page.expect_navigation()