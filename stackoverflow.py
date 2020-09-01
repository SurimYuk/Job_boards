import requests
from bs4 import BeautifulSoup  #Exploring and extracting data

JOB_URL = f"https://stackoverflow.com/jobs/"

def get_last_page(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)

def extract_job(html):
  title = html.find("h2").find("a")["title"]

  company, location = html.find("h3").find_all("span", recursive=False)
  company = company.get_text(strip=True)
  location = location.get_text(strip=True)
  
  job_id = html["data-jobid"]
  
  return {"title":title, "company":company, "location":location, "link":f"{JOB_URL}{job_id}"}

def extract_jobs(last_page, url):
  jobs= []

  for page in range(last_page):
    print(f"Scrapping SO: page {page+1}")
    result = requests.get(f"{url}&pg={page+1}")
    soup = BeautifulSoup(result.text, "html.parser")
    job_cards = soup.find_all("div", {"class":"-job"})
    for job_card in job_cards:
      job = extract_job(job_card)
      jobs.append(job)

  return jobs


def get_jobs(word):
  url = f"https://stackoverflow.com/jobs?q={word}"
  last_page = get_last_page(url)
  jobs = extract_jobs(last_page, url)
  return jobs