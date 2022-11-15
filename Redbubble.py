from selenium import webdriver
import chromedriver_autoinstaller
import time
import glob


def uploadToRedbubble():
    # Set the Redbubble login information
    username = 'KatieDeForest@outlook.com'
    password = 'SfxZPCK5c$N#VKG&dhI*xLfWIINB3FWqmapXN5%7Z0k9iLfjuLfYpW9ImHpyy6#9#Snmzzk%qsfLZ9JP*vzUGgLu2uVvauvUhNFYAlzJLAYHPuZ&n!&Nlv6F$5tbP09t'
    design_upload = glob.glob("resources/*.png")
    print(design_upload)
    base_design_url = 'https://www.redbubble.com/portfolio/images/128434997-beautiful-young-woman/duplicate'

    # Check if the current version of chromedriver exists and if it doesn't exist, download it automatically,then add chromedriver to path
    # chromedriver_autoinstaller.install()
    # # Create new Instance of Chrome
    # driver = webdriver.Chrome()
    #
    # # Open the base design webpage
    # driver.get(base_design_url)
    # # find username/email field and send the username itself to the input field
    # driver.find_element_by_id("ReduxFormInput1").send_keys(username)
    # # find password input field and insert password as well
    # driver.find_element_by_id("ReduxFormInput2").send_keys(password)
    # # click login button
    # driver.find_element_by_css_selector(
    #     ".app-ui-components-Button-Button_button_1_MpP.app-ui-components-Button-Button_primary_pyjm6.app-ui-components-Button-Button_padded_1fH5b").click()
    # time.sleep(20)

    for i in design_upload:
        # Take the design name and removing the extension
        img_name = i[10:].split('.')[0]
        url_img = i
        title = i[10:].split(',', 1)[0]
        tags = i[10:].split(',', 1)[1]
        print("img_name: ", img_name)
        print("url_img: ", url_img)
        print("title: ", title)
        print("tags: ", tags)
        # desc = 'Made with <3'
        # driver.get(base_design_url)
        # time.sleep(1)
        # # Filling the title form
        # element = driver.find_element_by_id('work_title_en')
        # element.clear()
        # element.send_keys(title)
        # # Filling the tag form
        # element = driver.find_element_by_id('work_tag_field_en')
        # element.clear()
        # element.send_keys(tags)
        # # Filling the description form
        # element = driver.find_element_by_id('work_description_en')
        # element.clear()
        # element.send_keys(desc)
        # # Upload the image design
        # driver.find_element_by_id('select-image single').send_keys(url_img)
        # # Click the Declaration form
        # driver.find_element_by_id('rightsDeclaration').click()
        # # Let the design upload process finished
        # time.sleep(30)
        # # Submit the work
        # driver.find_element_by_id('submit-work').click()
        #
        # # Let the whole process finish before move on to the next design
        # time.sleep(30)
