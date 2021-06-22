import win32gui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
##################
driver = webdriver.Firefox()
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

siteOpt = ["1) LinkedIn", "2) Indeed", "3) Other"]
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
#print("ARE YOU SIGNED IN?\nY/N")
#signedIn = input()
print("HOW MANY JOBS WOULD YOU LIKE TO APPLY FOR? \n *LIMIT 50*")
hmt = int(input())

while hmt > 51:
    print("PLEASE ENTER A NUMBER LESS THAN 50")
    hmt = int(input())
    if hmt < 51:
        break


##################
def main_fcs():
    if jobSite in jobUrl:
        print("WORKS!")
    else:
        print("NOTHING!")


##########
# INIT DEF
#########

main_fcs()
