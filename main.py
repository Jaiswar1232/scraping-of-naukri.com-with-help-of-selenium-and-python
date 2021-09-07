
from selenium import webdriver
from  bs4 import BeautifulSoup
from selenium.webdriver.support.select import Select
import requests
from openpyxl import Workbook
import time
import pandas as pd 


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.naukri.com/app-jobs-in-mumbai")
time.sleep(7)

t=[]
list_of_jobs=driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
for title in list_of_jobs:
     t.append(title.text)
    #print(title.text)

d=[]
job_description=driver.find_elements_by_xpath("//div[@class='job-description fs12 grey-text']")
for description in job_description:
    d.append(description.text)
    #print(description.text)

e=[]
job_expereince=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi experience']")
for expereince in job_expereince:
    e.append(expereince.text)
    #print(expereince.text)

l=[]
job_location=driver.find_elements_by_xpath("//li[@class='fleft grey-text br2 placeHolderLi location']")
for location in job_location:
    l.append(location.text)
    #print(location.text)

s=[]
job_skills=driver.find_elements_by_xpath("//ul[@class='tags has-description']")
for skills in job_skills:
    s.append(skills.text)
    #print(skills.text)

finallist=zip(t,d,e,l,s)

wb=Workbook()
sh1=wb.active

for x in list(finallist):
    sh1.append(x)

wb.save("finallist.xlsx")


