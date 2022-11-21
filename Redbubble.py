import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import glob

from selenium.webdriver.common.by import By

def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)

def uploadToRedbubble():
    # Set the Redbubble login information
    username = 'KatieDeForest@outlook.com'
    password = 'SfxZPCK5c$N#VKG&dhI*xLfWIINB3FWqmapXN5%7Z0k9iLfjuLfYpW9ImHpyy6#9#Snmzzk%qsfLZ9JP*vzUGgLu2uVvauvUhNFYAlzJLAYHPuZ&n!&Nlv6F$5tbP09t'
    design_upload = glob.glob("resources/*.png")
    print(design_upload)

    # Check if the current version of chromedriver exists and if it doesn't exist, download it automatically,then add chromedriver to path
    driver = uc.Chrome(use_subprocess=True)
    wait = WebDriverWait(driver, 20)
    base_design_url = 'https://www.redbubble.com/portfolio/images/128434997-beautiful-young-woman/duplicate'
    driver.get(base_design_url)
    # Wait for cookies to appear and click on decline lol
    time.sleep(5)
    wait.until(EC.visibility_of_element_located((By.ID, "CybotCookiebotDialogBodyButtonDecline"))).click()
    # find username/email field and send the username itself to the input field
    wait.until(EC.visibility_of_element_located((By.ID, "ReduxFormInput1"))).send_keys(username)
    # find password input field and insert password as well
    wait.until(EC.visibility_of_element_located((By.ID, "ReduxFormInput2"))).send_keys(password)
    # click login button
    driver.find_element(By.CSS_SELECTOR,
                        ".app-ui-components-Button-Button_button_1_MpP.app-ui-components-Button-Button_primary_pyjm6"
                        ".app-ui"
                        "-components-Button-Button_padded_1fH5b").click()
    time.sleep(3)

    for i in design_upload:
        # Take the design name and removing the extension
        img_name = i[10:]
        url_img = i
        title = i[10:].split(',', 1)[0]
        tags = i[10:len(i)-4].split(',', 1)[1]
        print("img_name: ", img_name)
        print("url_img: ", url_img)
        print("title: ", title)
        print("tags: ", tags)
        # desc = 'Made with <3'
        # driver.get(base_design_url)
        time.sleep(1)
        # Filling the title form
        element = wait.until(EC.visibility_of_element_located((By.ID, "work_title_en")))
        element.clear()
        element.send_keys(title)
        # Filling the tag form
        element = wait.until(EC.visibility_of_element_located((By.ID, "work_tag_field_en")))
        element.clear()
        element.send_keys(tags)
        # Filling the description form
        element = wait.until(EC.visibility_of_element_located((By.ID, "work_description_en")))
        element.clear()
        element.send_keys("Made by Katie")
        # Upload the image design
        wait.until(EC.visibility_of_element_located((By.ID, "select-image-base"))).send_keys('E:\Documents\VSCode\AIHelper\resources\Black Hole, space, ai, blackhole.png')
        # Click the Declaration form
        wait.until(EC.visibility_of_element_located((By.ID, "rightsDeclaration"))).click()
        # Let the design upload process finished
        time.sleep(30)
        # Submit the work
        wait.until(EC.visibility_of_element_located((By.ID, "submit-work"))).click()

        # Let the whole process finish before move on to the next design
        time.sleep(30)
