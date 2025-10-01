from Crawler import Crawler
import time

def use_search_box(crawler : Crawler, query):
    textBox = crawler.find("input[id^='jobs-search-box-keyword-id']")[0]
    textBox.fill(query)
    with crawler.expect_navigation():
        textBox.press("Enter")

def scroll_job_list(crawler : Crawler):
    jobList = crawler.find("ul.semantic-search-results-list")[0]
    height = jobList.evaluate("e => e.scrollHeight")
    scrollPos = 0
    while scrollPos < height:
        scrollPos = min(height, scrollPos + 600)
        jobList.evaluate(f"e => e.scrollTop = {scrollPos}")
        time.sleep(0.05)
    jobList.evaluate("e => e.scrollTop = 0")
    time.sleep(1)

def search_jobs(crawler : Crawler):
    use_search_box(crawler, "software engineer")
    #Load results by scrolling the list
    scroll_job_list(crawler)
    #Return jobs
    return crawler.find("a.job-card-job-posting-card-wrapper__card-link")

def get_job_title(job):
    title = job.query_selector("div.job-card-job-posting-card-wrapper__title").query_selector("strong").inner_html()
    start = title.find('>')
    end = title.rfind('<')
    return title[start+1:end]

if __name__ == "__main__":
    url = "https://www.linkedin.com/jobs/"
    crawler = Crawler()
    crawler.goto(url)
    
    jobs = search_jobs(crawler)
    for job in jobs:
        print(get_job_title(job))
        with crawler.expect_navigation():
            job.click()
        time.sleep(0.5)
    
    input("...")
    crawler.close()
