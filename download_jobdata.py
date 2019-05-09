from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
from os.path import dirname, abspath
import time, logging, sys,traceback
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

USERNAME = "f0rt3stpurp0s3@gmail.com"
PASSWORD = "f0rt3stpurp0s3"
LOGIN_URL = "https://www.kaggle.com/account/login?isModal=true&returnUrl=/madhab/jobposts/downloads/data job posts.csv/1"
URL = "https://www.kaggle.com/madhab/jobposts"

parentDir = dirname(abspath(__file__))

prefs = {'download.default_directory' : parentDir}
options = Options()
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(chrome_options=options)

try:
	#got to login url, and after done login it will return to download csv right away
	logging.info("REQUEST TO LOGIN PAGE  : {}".format(LOGIN_URL))
	driver.get(LOGIN_URL)
	#key in login details and ENTER
	input_username = driver.find_element_by_id("username-input-text")
	input_username.send_keys(USERNAME)
	input_password = driver.find_element_by_id("password-input-text")
	input_password.send_keys(PASSWORD)
	input_password.send_keys(Keys.RETURN)
	logging.info("DOWNLOADING DATA SOURCE")

	#wait for file to download
	file_path = parentDir+"/data job posts.csv.zip"
	file_exist = False
	while not os.path.exists(file_path):
	    time.sleep(1)

	if os.path.isfile(file_path):
	    file_exist = True
	    logging.info("FILE NAME :{} IS DOWNLOADED".format("/data job posts.csv.zip"))
	else:
	    raise ValueError("%s ISN'T A FILE!" % file_path)
except Exception as e:
	logging.info(traceback.format_exc())

driver.quit()
