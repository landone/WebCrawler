from Crawler import Crawler
from urllib.parse import urljoin

def crawl(url):
    crawler = Crawler()
    crawler.goto(url)
    elements = crawler.find("a[data-test-selector='recommended-channel']")
    selectedElement = None
    for element in elements:
        href = element.get_attribute("href")
        element.evaluate("el => el.style.backgroundColor = 'yellow'")
        if href == '/northernlion':
            selectedElement = element
    input("Press Enter to close the browser...")
    if selectedElement:
        selectedElement.click()
        crawler.wait_for_load()
    input("Press Enter to close the browser...")
    crawler.close()
    return 0

if __name__ == "__main__":
    start_url = "https://twitch.com"
    crawl(start_url)
