import requests
from bs4 import BeautifulSoup as bs
import re
import random

search_url = "https://www.104.com.tw/job/6495v?jobsource=2018indexpoc"
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4'}
response = requests.get(search_url, headers = head)
response.encoding = 'utf8'
soup = bs(response.text)
#先從內層開始抓
job_name = soup.title.text.split("｜")[0]
job_company = soup.title.text.split("｜")[1]
job_region = soup.title.text.split("｜")[2].split("－")[0]
job_type = soup.find("dd",class_="cate").find("span").text

# job_type = .text.strip("\n").split(" ")
job_addr = soup.find("dd",class_="addr").text.strip().split("\n")[0]
job_salary = soup.find("dd", class_="salary").text
if "待遇面議" in job_salary:
        job_salary = "待遇面議"

# print("job_name :", job_name)
# print("job_company:", job_company)
# print("job_region:", job_region)
print("job_type :", job_type)
# print("job_addr:" ,job_addr)
print("job_salary:" ,job_salary)

job_exp = soup.find_all("dd")
# print('job_exp:',job_exp[11].text)