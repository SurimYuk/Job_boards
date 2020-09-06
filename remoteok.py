import requests
from bs4 import BeautifulSoup

def extract_job(html):
  title = html.find("h2").string
  company = html.find("h3").string
  location = html.find("div",{"class":"location"})
  if location is None:
    location = "Remote"
  else:
    location = location.string
  link = html["data-url"]

  return {"title":title, "company":company, "location":location, "link":f"https://remoteok.io{link}"}

def extract_jobs(url):
  jobs = []
  print("Scrapping from remoteok.")
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  job_cards = soup.find_all("tr",{"class":"job"})
  for job_card in job_cards:
    job = extract_job(job_card)
    jobs.append(job)
  return jobs

def get_jobs(word):
  url = f"https://remoteok.io/remote-{word}-jobs"
  jobs = extract_jobs(url)
  return jobs
