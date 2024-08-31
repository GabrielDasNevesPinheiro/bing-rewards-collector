from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

def click_items(clickables: list):
    for clickable in clickables:
        clickable.click()

def open_tab(driver: WebDriver):
    driver.execute_script('window.open('')')

def close_tab(driver: WebDriver):
    driver.close()

def clean_tabs(driver: WebDriver):
    for handle in driver.window_handles:
        driver.switch_to.window(handle)

        if len(driver.window_handles) == 1:
            break
        
        driver.close()

queries = [x.strip() for x in open('queries', 'r', encoding="utf-8").readlines()]
def build_query(query: str):
    splitted = query.split(" ")
    return f"https://www.bing.com/search?q={query}&form=QBLH&sp=-1&ghc=1&lq=0&pq={splitted[0]}+{splitted[1]}&sc=11-14&qs=n&sk=&cvid=9AF4D34E0A56422AA2BC643057E3D75B&ghsh=0&ghacc=0&ghpl="

options = webdriver.EdgeOptions()
options.use_chromium = True
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
options.add_argument("headless")
options.add_argument("disable-gpu")
options.add_argument("--log-level=3")

target = "https://rewards.bing.com/?ref=rewardspanel"
driver = webdriver.Edge(options=options)
driver.get(target)

first_section = driver.find_elements(By.XPATH, '//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card')
second_section = driver.find_elements(By.XPATH, '//*[@id="more-activities"]/div/mee-card')


click_items(first_section)
click_items(second_section)

print("ALL CLICKS COLLECTED")

clean_tabs(driver)

print("STARTING COLLECTING SEARCHES")

limit = 90
for query in queries:
    open_tab(driver)
    driver.switch_to.window(driver.window_handles[1])
    driver.get(build_query(query))
    sleep(10)
    clean_tabs(driver)
    calculated = (queries.index(query) + 1) * 3
    print(f"SEARCH DONE FOR QUERY -> {queries.index(query)}: {calculated} score")
    if calculated >= limit:
        break

driver.quit()