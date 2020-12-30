from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path='/home/mr-radium/Python/Web Scraping/chromedriver')
browser.get('https://forms.gle/wh9JrrnBYEUJgPPF9')

short_answer = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
long_answer = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea'
multiple_choice = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[2]/div/span'
check_boxes = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[1]/label/div/div[2]/div/span'
dropdown = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div[1]'
dropdown_option = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[2]/div[5]/span'
submit = '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span'


browser.find_element_by_xpath(short_answer).send_keys('Did it work?')
browser.find_element_by_xpath(long_answer).send_keys('Yes, it did')
browser.find_element_by_xpath(multiple_choice).click()
browser.find_element_by_xpath(check_boxes).click()
browser.find_element_by_xpath(dropdown).click()
time.sleep(0.5)
browser.find_element_by_xpath(dropdown_option).click()
time.sleep(1)
browser.find_element_by_xpath(submit).click()