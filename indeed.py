import requests
from bs4 import BeautifulSoup  #Exploring and extracting data

LIMIT = 50
JOB_URL = "https://www.indeed.com/viewjob?jk="


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    last_page = pages[-1]

    return last_page


def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]

    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    try:
      if company_anchor is not None:
          company = company_anchor.string
      else:
          company = company.string
      company = company.strip()
    except Exception as ex:
      print(ex)
      print(title)

    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]

    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"{JOB_URL}{job_id}"
    }


def extract_jobs(last_page, url):
  jobs = []
    
  for page in range(last_page):
    print(f"Scrapping Indeed: page {page}")
    result = requests.get(f"{url}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    job_cards = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    for job_card in job_cards:
      job = extract_job(job_card)
      jobs.append(job)

  return jobs

def get_jobs(word):
  url = f"https://www.indeed.com/jobs?q={word}&limit={LIMIT}"
  last_page = get_last_page(url)
  jobs = extract_jobs(last_page, url)
  return jobs