import webbrowser
import ajs_indeed
import win32gui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

##################
#driver = webdriver.Firefox()

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

        ajs_indeed

    else:
        print("NOTHING!")


##########
# INIT DEF
#########

main_fcs()
