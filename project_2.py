import re
import time
import traceback
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os

def getFiles(archive):
    list_of_links = []
    try:
        with open(archive,"r") as f:
            list_of_links = extract_youtube(f.read().split("\n"))
            f.close()
    except:
        print("Couldn't find any file in this path.")
    return list_of_links

def extract_youtube(s):
    list_links = []
    text = s
    for i in s:
        match = re.search('(h[\S]*)',i)
        list_links.append(match.group(0))
    return list_links

def headless_config(browser,path_os):
    regex_dir_pattern = r'(^.*\\)\w+\.\w+$'
    m = re.search(regex_dir_pattern, path_os)
    directory = m.group(1)
    chrome_options = Options()
    chrome_options.headless = False
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--verbose')

    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": directory,
        "directory_upgrade": True,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })
    chrome_options.add_argument('--disable-software-rasterizer')
    return chrome_options
def download(browser,download_dir,link):

    browser = webdriver.Chrome(
        executable_path=r"C:\Users\Gustavo\.wdm\drivers\chromedriver\win32\83.0.4103.39\chromedriver.exe",
        options=headless_config(browser,download_dir))

    browser.get(link)
    time.sleep(120)
    browser.close()


def youtube_bot(page,link,download_dir):
    exception_handled = False
    chrome_options = Options()
    chrome_options.headless = False
    driver = webdriver.Chrome(executable_path=r"C:\Users\Gustavo\.wdm\drivers\chromedriver\win32\83.0.4103.39\chromedriver.exe",options=chrome_options)
    driver.maximize_window()

    driver.get(page)
    driver.implicitly_wait(5)
    assert "Youtube2mp3 :: convert YouTube videos to mp3" in driver.title

    inputBox_id = "url_url"

    inputbox = driver.find_element_by_id(inputBox_id)
    inputbox.clear()
    inputbox.send_keys(link)
    driver.implicitly_wait(5)
    button = driver.find_element_by_xpath("/html/body/div[2]/div/form/fieldset/div[2]/div/button")
    button.click()
    class_name = "btn btn-success"
    attribute_xpath = '/html/body/div[2]/div/div/div/div[1]/h1'
    time.sleep(10)
    sec = re.findall("\d",driver.find_element_by_id("tLeft").text)
    left = (int(sec[0])*60)+(int(sec[1])*60)+int(sec[2]+sec[3])
    time.sleep(left+10)
    #element = WebDriverWait(driver,left).until(EC.presence_of_element_located((By.CLASS_NAME,class_name)))
    button_xpath = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/a")
    assert "Thanks for using Youtube2mp3.net!" in driver.find_element_by_class_name("col-lg-12").text
    link_download = button_xpath.get_attribute("href")
    download(driver,download_dir,link_download)
    driver.close()


def main():
    page = input("Insert the page which perform convertion from video to Mp3 through Youtube platform")
    archive = input("Insert the path where the links are: ")
    #page = "https://www.youtube2mp3.net/"
    #archive =r"C:\Users\Gustavo\Music\mp3\musicas.txt"
    listOfyoutube = getFiles(archive)

    listOfyoutube = list(filter(lambda x: len(x) == 28, getFiles(archive)))
    listplaylists = list(filter(lambda x: len(x) > 28, getFiles(archive)))

    for link in range(6,7):

        try:
            
            youtube_bot(page,listOfyoutube[link],archive)
        except NoSuchElementException:
            regex_dir_pattern = r'(^.*\\)\w+\.\w+$'
            m = re.search(regex_dir_pattern, archive)
            directory = m.group(1)
            w = open(directory + r"\failedVideos.txt", "a")
            print(listOfyoutube[link], end="\n", file=w)
            w.close()
            traceback.format_exc()


if __name__ == "__main__":
    main()

#continue loop after exception
#implement a function that checks if the file is already downloaded to finish running
