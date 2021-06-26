import time
import webbrowser
from pywin.tools import browser
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.keys import Keys


options = webdriver.FirefoxOptions()
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)

siteOpt = [
    "1) LinkedIn",
    "2) Indeed",
    "3) Other"
]
jobUrl = {
    "1": "https://www.linkedin.com/jobs/",
    "2": "https://www.indeed.com/"
}

##################
##################
print("WELCOME TO AUTO JOB SEARCH!\n" + "=" * 30)

print("WHICH JOB SITE WOULD YOU LIKE TO USE TODAY?")
print(*siteOpt, sep="\n")
jobSite = input()

while int(jobSite) > 2:
    print("ERROR: PLEASE ENTER A CONSOLE NUMBER!")
    jobSite = input()

sel_jobSite = jobSite
print("WHAT JOB TITLE DO YOU WANT TO APPLY FOR?")
jobTitle = input()
print("HOW MANY JOB LISTINGS WOULD YOU LIKE TO APPLY FOR? \n *LIMIT 50*")
hmt = int(input())

# LIMIT CHECK
while hmt > 51:
    print("PLEASE ENTER A NUMBER LESS THAN 50")
    hmt = int(input())
    if hmt < 51:
        break


##################

# init job srch
def main_fcs():
    if jobSite in jobUrl:
        webbrowser.open(jobUrl[sel_jobSite])

        time.sleep(10)
        jobTitle_fill = driver.find_element_by_xpath('//input[@id="text-input-what"]')
        jobTitle_fill.send_keys(jobTitle)

        driver.close()

    else:
        print("NOTHING!")


##########
# INIT DEF
#########

main_fcs()
