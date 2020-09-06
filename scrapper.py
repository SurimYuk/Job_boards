from stackoverflow import get_jobs as get_so_jobs
from wwr import get_jobs as get_wwr_jobs
from remoteok import get_jobs as get_remoteok_jobs

def get_jobs(word):
  so_jobs = get_so_jobs(word)
  wwr_jobs = get_wwr_jobs(word)
  remo_jobs = get_remoteok_jobs(word)
  jobs = so_jobs + wwr_jobs + remo_jobs
  return jobs