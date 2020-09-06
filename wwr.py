import requests
from bs4 import BeautifulSoup

def extract_job(li):
  title = li.find("span",{"class","title"}).get_text()
  company = li.find("span",{"class","company"}).string
  region = li.find("span",{"class":"region"})
  if region is None:
    location = "Remote"
  else:
    location = region.string
  link = li.find_all("a")
  link = link[-1]
  link = link["href"]

  return {"title":title, "company":company, "location":location, "link":f"https://weworkremotely.com{link}"}

def extract_jobs(url):
  jobs = []
  print("Scrapping from wwr.")
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  job_container = soup.find("section", {"id":"category-2"})
  job_cards = job_container.find_all("li",{"class","feature"})
  for job_card in job_cards:
    job = extract_job(job_card)
    jobs.append(job)
  return jobs

def get_jobs(word):
  url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  jobs = extract_jobs(url)
  return jobs