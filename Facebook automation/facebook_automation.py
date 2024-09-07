from tkinter.tix import WINDOW
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time

service = Service(executable_path='C:\\Users\\Akshat S\\Desktop\\excel report\\chromedriver-win64\\chromedriver.exe')
options = webdriver.ChromeOptions()
##>>> popup block
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-notifications')
options.add_argument('--disable-infobars')

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.facebook.com/")

try:
    email_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "email"))).send_keys("akkis0803try@gmail.com")

    password_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "pass"))).send_keys("Akss@0803#Try")

    time.sleep(5)

    driver.maximize_window()

    login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.NAME, "login"))).click()

    time.sleep(5)

    video_btn = "//a[@href='https://www.facebook.com/watch/']//div[@class='x6s0dn4 x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x9f619 x78zum5 x1q0g3np x1iyjqo2 xs83m0k x1qughib xat24cr x11i5rnm x1mh8g0r xdj266r xeuugli x18d9i69 x1sxyh0 xurb0ha xexx8yu x1n2onr6 x1ja2u2z x1gg8mnh']"
    click = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, video_btn))).click()

    time.sleep(5)

    stopScrolling = 0
    while True:
        stopScrolling += 1
        driver.execute_script("window.scrollBy(0,4)")
        time.sleep(0.01)
        if stopScrolling > 700:
            break
    time.sleep(3)


    stopScrolling = 0
    while True:
        stopScrolling += 1
        driver.execute_script("window.scrollBy(0,-4)")
        time.sleep(0.01)
        if stopScrolling > 700:
            break
    time.sleep(4)

    Main_Homebt_Path = "//a[@aria-label='Home']"
    click = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, Main_Homebt_Path))).click()

    time.sleep(5)

    stopScrolling = 0
    while True:
        stopScrolling += 1
        driver.execute_script("window.scrollBy(0,4)")
        time.sleep(0.01)
        if stopScrolling > 700:
            break
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, 0)")

    time.sleep(5)

    myprofile_path = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]"
    driver.find_element(By.XPATH, myprofile_path).click()

    time.sleep(5)
    driver.back()

    time.sleep(5)
    friends = "//body/div/div/div/div/div/div/div/div/div/div/div[@aria-label='Shortcuts']/div/div/div/div/div[@data-visualcompletion='ignore-dynamic']/div/div[1]/ul[1]/li[2]/div[1]/a[1]/div[1]"
    driver.find_element(By.XPATH, friends).click()

    time.sleep(5)
    driver.back()

    memories = "//body/div/div/div/div/div/div/div/div/div/div/div[@aria-label='Shortcuts']/div/div/div/div/div[@data-visualcompletion='ignore-dynamic']/div/div/ul/li[4]/div[1]/a[1]/div[1]"
    driver.find_element(By.XPATH, memories).click()

    time.sleep(5)
    driver.back()

    saved = "//body/div/div/div/div/div/div/div/div/div/div/div[@aria-label='Shortcuts']/div/div/div/div/div[@data-visualcompletion='ignore-dynamic']/div/div/ul/li[5]/div[1]/a[1]/div[1]"
    driver.find_element(By.XPATH, saved).click()

    time.sleep(5)
    driver.back()

    groups = "(//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[6]/div[1]/a[1]/div[1])"
    driver.find_element(By.XPATH, groups).click()

    time.sleep(5)
    driver.back()

    marketp = "(//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[8]/div[1]/a[1]/div[1])"
    driver.find_element(By.XPATH, marketp).click()

    time.sleep(5)

    stopScrolling = 0
    while True:
        stopScrolling += 1
        driver.execute_script("window.scrollBy(0,4)")
        time.sleep(0.01)
        if stopScrolling > 700:
            break
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, 0)")

    time.sleep(5)
    driver.back()

    feeds = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[9]/div[1]/a[1]/div[1]"
    driver.find_element(By.XPATH, feeds).click()

    time.sleep(5)
    driver.back()

    seemore = "(//body/div/div/div/div/div/div/div/div/div/div/div[@aria-label='Shortcuts']/div/div/div/div/div[@data-visualcompletion='ignore-dynamic']/div/div/div[@data-visualcompletion='ignore-dynamic']/div[@role='button']/div[1])"
    driver.find_element(By.XPATH, seemore).click()

    time.sleep(5)

    events = "(//body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[12]/div[1]/a[1]/div[1])"
    driver.find_element(By.XPATH, events).click()

    time.sleep(5)
    driver.back()

    search = "//input[@placeholder='Search Facebook']"
    driver.find_element(By.XPATH, search).send_keys("Aman Sharma")

    time.sleep(3)

    sbt = "(//body/div/div/div/div/div[@role='banner']/div[@aria-hidden='false']/div/div/div/div/div/div/div/ul[@aria-label='8 suggested searches']/li[1]/div[1]/a[1]/div[1]/div[1])"
    driver.find_element(By.XPATH, sbt).click()
    
    time.sleep(3)

    srcpeople = "(//body/div/div/div/div/div/div/div/div/div/div[@aria-label='Result filters']/div/div/div/div/div/div/div/div[@role='list']/div[3]/div[1]/a[1]/div[1])"
    driver.find_element(By.XPATH, srcpeople).click()

    time.sleep(4)

    stopScrolling = 0
    while True:
        stopScrolling += 1
        driver.execute_script("window.scrollBy(0,4)")
        time.sleep(0.01)
        if stopScrolling > 700:
            break
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, 0)")

    time.sleep(4)
    driver.back()

    main_friendslogo = "//a[@aria-label='Friends']"
    driver.find_element(By.XPATH, main_friendslogo).click()

    time.sleep(4)

    main_grouplogo = "//a[@aria-label='Groups']"
    driver.find_element(By.XPATH, main_grouplogo).click()

    time.sleep(4)
    driver.back()

    Main_Homebt_Path = "//a[@aria-label='Home']"
    click = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, Main_Homebt_Path))).click()

    time.sleep(4)
    try:
        like = "(//body/div/div/div/div/div/div/div/div/div/div/div[@role='main']/div/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[13]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1])"
        driver.find_element(By.XPATH, like).click()

        print("liked successful")

    except WebDriverException as e:
        print(f"failed! Error:{e}")

    time.sleep(4)

    Account = "(//body/div/div/div/div/div[@role='banner']/div/div[@aria-label='Account controls and settings']/span[1])"
    driver.find_element(By.XPATH, Account).click()

    time.sleep(5)

    logout_path = "//div[@data-nocookies='true']//div[@class='x6s0dn4 x1q0q8m5 x1qhh985 xu3j5b3 xcfux6l x26u7qi xm0m39n x13fuv20 x972fbf x9f619 x78zum5 x1q0g3np x1iyjqo2 xs83m0k x1qughib xat24cr x11i5rnm x1mh8g0r xdj266r xeuugli x18d9i69 x1sxyh0 xurb0ha xexx8yu x1n2onr6 x1ja2u2z x1gg8mnh']"
    driver.find_element(By.XPATH, logout_path).click()

    print("operations done successfully")

except WebDriverException as e:
    print(f"failed! Error:{e}")
