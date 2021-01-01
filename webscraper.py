from selenium import webdriver
import time
# You would need time package while dealing with drop-downs
browser = webdriver.Chrome(executable_path='/home/mr-radium/Utilities/Chrome Driver/chromedriver') # This should work if you have the ChromeDriver in the same directory of your script.
# But in case it throws and error, Try this:
#browser = webdriver.Chrome(executable_path='/path/to/your/ChromeDriver')
browser.get('https://forms.gle/wh9JrrnBYEUJgPPF9')

# Make a variable and assign the xpath to it that you just copied
# I have named it 'short_answer' and assigned the xpath I just copied 
short_answer = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
