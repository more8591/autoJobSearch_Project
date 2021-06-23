# Indeed Auto Job Search
########################
import webbrowser
from autoJobSearch_Project.ajs_main import jobTitle

jobTitle_fill = webbrowser.find_element_by_id('text-input-what')
jobTitle_fill.write(jobTitle)


